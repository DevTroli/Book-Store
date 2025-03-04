from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import git
import logging

logger = logging.getLogger(__name__)

@csrf_exempt
def update(request):
    if request.method == "POST":
        try:
            repo_path = '/home/Troli/Book-Store'
            logger.info(f"Tentando atualizar o repositório em: {repo_path}")

            # Verifica se o diretório é um repositório Git válido
            try:
                repo = git.Repo(repo_path)
            except git.InvalidGitRepositoryError:
                logger.error(f"O diretório {repo_path} não é um repositório Git válido.")
                return HttpResponse("Invalid Git repository", status=500)

            # Verifica se o repositório tem um remote 'origin'
            if not repo.remotes:
                logger.error("Nenhum remote 'origin' configurado.")
                return HttpResponse("No remote 'origin' configured", status=500)

            origin = repo.remotes.origin

            # Tenta fazer o pull
            try:
                logger.info("Puxando as alterações do repositório remoto...")
                origin.pull()
                logger.info("Código atualizado com sucesso no PythonAnywhere")
                return HttpResponse("Updated code on PythonAnywhere", status=200)
            except git.GitCommandError as e:
                logger.error(f"Erro ao executar 'git pull': {e}")
                return HttpResponse(f"Git command error: {e}", status=500)
        except Exception as e:
            logger.error(f"Erro ao atualizar o código: {e}")
            return HttpResponse(f"Error updating code: {e}", status=500)
    else:
        logger.warning("Método de requisição não permitido")
        return HttpResponse("Couldn't update the code on PythonAnywhere", status=405) 
