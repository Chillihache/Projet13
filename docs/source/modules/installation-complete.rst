Installation complète
=====================

Avant de procéder à l'installation des différents outils, veuillez suivre les instructions du
guide de démarrage rapide.

Vérifier le Linting
-------------------

.. code-block:: bash

    cd /path/to/Projet13

.. code-block:: bash

    source venv/bin/activate

.. code-block:: bash

    flake8

Exécuter les tests unitaires et d'intégrations
----------------------------------------------

.. code-block:: bash

    cd /path/to/rojet13

.. code-block:: bash

    source venv/bin/activate

.. code-block:: bash

    pytest

Base de données
---------------

- SQLite3 CLI est prérequis

.. code-block:: bash

    cd /path/to/Projet13

- Ouvrir une session shell :

.. code-block:: bash

    sqlite3

- Se connecter à la base de données :

.. code-block:: bash

    .open oc-lettings-site.sqlite3

- Afficher les tables :

.. code-block:: bash

    .tables

- Afficher les colonnes dans le tableau des profiles :

.. code-block:: bash

    pragma table_info(profiles_profile);

- Lancer une requête :

.. code-block:: bash

    select user_id, favorite_city from profiles_profile where favorite_city like 'B%';

- Quitter le shell :

.. code-block:: bash

    .quit

Utilisation de l'admin Django
-----------------------------

Pour accéder à l'administrateur django, veuillez lancer votre serveur et accéder à l'adresse ci-dessous
dans votre navigateur :

http://localhost:8000/inconspicuous-admin/

Vous pouvez vous connecter avec les identifiants suivants :

- Utilisateur : admin
- Mot de passe : Abc1234!