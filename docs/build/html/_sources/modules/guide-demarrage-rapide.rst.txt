Guide de démarrage rapide
==========================


Prérequis
----------

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- Interpréteur Python, version 3.6 ou supérieure
- Un compte Sentry

Installation (macOS/Linux)
---------------------------

Pour installer rapidement et simplement le projet en local, vous pouvez suivre les étapes ci-dessous :

- Clonez le repository :

.. code-block:: bash

    cd /path/to/put/project/in

.. code-block:: bash

    git clone https://github.com/Chillihache/Projet13.git

- Créez un environnement virtuel :

.. code-block:: bash

    cd /path/to/Projet13

.. code-block:: bash

    python -m venv venv

- Activez l'environnement :

.. code-block:: bash

    source venv/bin/activate

- Installez les dépendances :

.. code-block:: bash

    pip install -r requirements.txt

- Créez un nouveau projet Sentry et récupérez le DNS.

- Renommez le fichier .env.sample en .env

- Remplir les champs "DJANGO_SECRET_KEY" et "DNS_SENTRY"

- Collectez les fichiers statiques :

.. code-block:: bash

    python manage.py collectstatic

- Lancez le serveur :

.. code-block:: bash

    python manage.py runserver

- Aller sur http://localhost:8000 dans votre navigateur.


Installation (Windows)
---------------------------

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel :

.. code-block:: shell

    .\venv\Scripts\Activate.ps1










