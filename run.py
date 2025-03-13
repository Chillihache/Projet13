import os
import subprocess
import sys
from decouple import config

"""
    Allows retrieving the latest version of the image from Docker Hub and starting a container
"""

IMAGE_NAME = config('IMAGE_NAME')


def check_env_file():
    """
        Check if the .env file exists, otherwise display an error.
    """
    if not os.path.exists(".env"):
        print("Error: The .env file was not found!")
        print("Please create a .env by copying .env.sample")
        sys.exit(1)


def pull_docker_image():
    """
        Fetch the latest version of the image from Docker Hub.
    """
    print("Fetching the image from Docker Hub...")
    subprocess.run(["docker", "pull", IMAGE_NAME], check=True)


def run_docker_container():
    """
        Run the container using .env and expose port 8000.
    """
    print("Launching the container...")
    subprocess.run(["docker", "run", "--env-file", ".env", "-p", "8000:8000", IMAGE_NAME],
                   check=True)


if __name__ == "__main__":
    check_env_file()
    pull_docker_image()
    run_docker_container()
