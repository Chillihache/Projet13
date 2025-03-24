Procédures de deploiement et gestion de l'application
======================================================

Dans cette page, je vous expliquerai comment est composée la pipeline CI/CL et comment l'utiliser avec Github Actions

Description de la pipeline GitHub actions
-----------------------------------------

La pipeline CI/CL se déclanche à chque push ou pull request et comprend 3 parties :

- Lancement des tests, vérification de la couverture (plus de 80%) et vérification du linting. (Sur toutes les branches)
- Conteneurisation avec Docker et envoie de l'image sur Docker Hub (Uniquement sur la branche "master")
- Déploiement de l'image en ligne via l'API de Render (Uniquement sur la branche "master")

Chaque étape de la pipeline ne se déclanche que si l'étape précédente est un succès

Configuration de la pipeline
----------------------------

Prérequis
~~~~~~~~~

- Un compte Github
- Un compte render avec, au minimum, le plan professionel (Pour utilisation de l'API)
- Un compte Docker Hub
- Docker Desktop installé sur sa machine

Configuration
~~~~~~~~~~~~~

- Pour avoir accès à la pipeline, forkez le projet sur votre compte Github
- Dans votre projet, sur Github, accédez à settings > Secrets and Variables > actions
- Ici, créez les repository secrets suivants : DJANGO_SECRET_KEY, DNS_SENTRY, DOCKERHUB_TOKEN, DOCKERHUB_USERNAME, RENDER_API_KEY, RENDER_OWNER_ID
- La pipeline est maintenant fonctionnelle et se déclenchera a chaque push ou pull requests.

Récupérer et lancer l'image Docker Hub
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Vous avez la possibilité de récupérer l'image stockée sur Docker Hub.

- Ouvrez Docker Desktop
- Allez dans votre repository local :

.. code-block:: bash

    cd /path/to/Projet13

- Remplissez le champ IMAGE_NAME dans votre .env (voir guide de démarrage rapide)
- Le nom de l'image devrait être votre_username_docker_hub/oc-lettings-site:latest
- Activez votre environment virtuel :

.. code-block:: bash

    source venv/bin/activate

- Puis lancer la commande suivante :

.. code-block::  bash

    python run.py

- Allez sur http://localhost:8000 dans votre navigateur



