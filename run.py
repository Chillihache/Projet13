import os
import subprocess
import sys

IMAGE_NAME = "chillihache/oc-lettings-site:latest"


def check_env_file():
    """Vérifie si le fichier .env existe, sinon affiche une erreur."""
    if not os.path.exists(".env"):
        print("Erreur : Le fichier .env est introuvable !")
        print("📌 Veuillez créer un .env en copiant .env.sample :")
        print("   cp .env.sample .env")
        sys.exit(1)


def pull_docker_image():
    """Récupère la dernière version de l'image depuis Docker Hub."""
    print("📥 Récupération de l'image depuis Docker Hub...")
    subprocess.run(["docker", "pull", IMAGE_NAME], check=True)


def run_docker_container():
    """Lance le conteneur en utilisant .env et expose le port 8000."""
    print("🚀 Lancement du conteneur...")
    subprocess.run(["docker", "run", "--env-file", ".env", "-p", "8000:8000", IMAGE_NAME], check=True)


if __name__ == "__main__":
    check_env_file()
    pull_docker_image()
    run_docker_container()
