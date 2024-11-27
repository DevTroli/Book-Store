# Book Store API

![GitHub repo size](https://img.shields.io/github/repo-size/DevTroli/Book-Store)
![GitHub stars](https://img.shields.io/github/stars/DevTroli/Book-Store)
![GitHub forks](https://img.shields.io/github/forks/DevTroli/Book-Store?style=social)

A Django REST framework-based API designed for managing a book store. It allows users to browse, order, and manage books, categories, and orders efficiently. The project provides a modular and scalable backend with robust testing and best practices.

# Tech Stack

- **Python** (v3.12)
- **Django** (v4.x)
- **Django REST Framework** (DRF)
- **PostgreSQL** (as the database)
- **pytest** (for testing)
- **factory-boy** and **Faker** (for generating test data)
- **Poetry** (for dependency management)

# Prerequisites

Before you begin, ensure you have met the following requirements:
* Python 3.12 installed on your system.
* PostgreSQL database configured and running.
* Poetry installed (`pip install poetry`).
* A machine running **Linux**, **macOS**, or **Windows** with the latest updates.

## Features

This project makes it easy to:
* Manage book categories, products, and orders through an API.
* Integrate user authentication for managing orders.
* Perform CRUD operations on books and categories.
* Place and manage orders with relational dependencies.
* Utilize automated testing for reliable development.

## Installing Book Store API

To install Book Store API, follow these steps:

### Clone the repository
```bash
git clone https://github.com/DevTroli/Book-Store.git
cd Book-Store
```

### Install dependencies
```bash
poetry install
```

#### Configure environment variables to create a .env
```bash
python contrib/envGen.py
# Don't forget to add your database access to .env
```

### Apply migrations
```bash
poetry run python manage.py migrate
```

### Create a superuser
```bash
poetry run python manage.py createsuperuser
```

### Run the server
```bash
poetry run python manage.py runserver
```

## Using Book Store API

To use Book Store API, follow these steps:

### Access the API
Start the server and navigate to `http://127.0.0.1:8000/api/v1/` to explore the available endpoints.

### Example: Creating an Order
Send a `POST` request to `/api/v1/orders/` with the following payload:
```json
{
  "products_id": [1, 2],
  "user": 1
}
```

### Running Tests
Run all tests using `pytest`:
```bash
poetry run pytest
```

Add custom configurations to your `pytest.ini` file as needed for better test management.

### Contributing to Book Store API

To contribute to Book Store API, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`.
4. Push to the original branch: `git push origin book-store-api/<location>`.
5. Create the pull request.

Alternatively, see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

### Contributors

Thanks to the following people who have contributed to this project:

* [@DevTroli](https://github.com/DevTroli/) 📖

Consider using the [All Contributors](https://github.com/all-contributors/all-contributors) specification and its [emoji key](https://allcontributors.org/docs/en/emoji-key).

### Contact

If you want to contact me, reach out at **pablotroli@outlook.com**.

### License

This project uses the following license: [MIT License](https://opensource.org/licenses/MIT).
