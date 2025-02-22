# Usar uma imagem base do Python que corresponda à versão do seu projeto
FROM python:3.12.1-slim as python-base

ENV PYTHONUNBUFFERED=1 \
  PYTHONDONTWRITEBYTECODE=1 \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.7.1 \
  POETRY_HOME="/opt/poetry" \
  POETRY_VIRTUALENVS_IN_PROJECT=true \
  POETRY_NO_INTERACTION=1 \
  PYSETUP_PATH="/opt/pysetup" \
  VENV_PATH="/opt/pysetup/.venv"

# Prepend poetry and venv to path
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

RUN apt-get update \
  && apt-get install --no-install-recommends -y \
  # deps for installing poetry
  curl \
  # deps for building python deps
  build-essential

# Instalar poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

RUN apt-get update \
  && apt-get -y install libpq-dev gcc \
  && pip install psycopg2

# copy project requirement files here to ensure they will be cached.
WORKDIR $PYSETUP_PATH
COPY poetry.lock pyproject.toml ./

# install runtime deps - uses $POETRY_VIRTUALENVS_IN_PROJECT internally
RUN poetry install --no-dev

# quicker install as runtime deps are already installed
RUN poetry install

COPY . /app/

WORKDIR /app

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
