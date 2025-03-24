## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure
- Sentry

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/Chillihache/Projet13.git`

#### Créer l'environnement virtuel

- `cd /path/to/Projet13`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Projet13`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- Créer un nouveau projet Django avec Sentry
- Créer un copie du fichier ".env.sample", la renommer ".env" et remplir les champs "DJANGO_SECRET_KEY" et "DNS_SENTRY"
- `python manage.py collectstatic`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.

#### Linting

- `cd /path/to/Projet13`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/rojet13`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Déploiement

#### Fonctionnement du déploiement automatisée

La pipeline Github Actions possède 3 jobs principales. Elle vérifie l'ensemble des tests, le linting, la couverture de tests (80% min), créer une image sur Dockerhub puis déploie l'image sur render.
La pipeline se déclenche à chaque push ou pull requests. Seul la branche master est conteneurisée et déployée.

#### Prérequis

- Un compte render avec le plan profesionel de render (Pour l'utilisation de l'API)
- Un compte Dockerhub
- Docker Desktop

#### Configuration du déploiement automatisé

- Pour avoir accès à la pipeline, forkez le repository Github sur votre Github.
- Sur votre repository Github, accédez à settings > Secrets and variables > actions.
- Créez les repository secrets suivants : DJANGO_SECRET_KEY, DNS_SENTRY, DOCKERHUB_TOKEN, DOCKERHUB_USERNAME, RENDER_API_KEY, RENDER_OWNER_ID.
- La pipeline est maintenant fonctionnelle pour les push et pull requests.

#### Récupérer l'image sur Docker Hub en local.

- Ouvrez Docker Desktop
- `cd /path/to/Projet13`
- Remplissez le champ IMAGE_NAME dans le fichier .env.
- `source venv/bin/activate`
- `python run.py`
- Allez sur `http://localhost:8000` dans un navigateur.

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`
