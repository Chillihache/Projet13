Structure et modèles de la base de données
===========================================

Ce projet utilise SQLite3 comme système de gestion de base de données

Tables principales de la base de données
----------------------------

- **auth_user** : Stocke les informations des utilisateurs.
- **profiles_profile** : Associe des informations supplémentaires aux utilisateurs.
- **lettings_adress** : Contient les informations relative à l'adresse des locations
- **lettings_letting** : Contient les informations des locations



Modèle User :
-------------

- **id :** int
- **password :** varchar
- **last_login :** datetime
- **is_superuser :** bool
- **username :** varchar
- **last_name :** varchar
- **email :** varchar
- **is_staff :** bool
- **is_active :** bool
- **date joined :** datetime
- **first_name :** varchar

Modèle Profile :
----------------

- **id :** int
- **user_id :** int (Clé étrangère vers le modèle User)
- **favorite_city :** varchar

Modèle Address :
----------------

- **id :** int
- **number :** int
- **street :** varchar
- **city :** varchar
- **state :** varchar
- **zip_code :** int
- **country_iso_code :** varchar

Modèle Letting :
----------------

- **id :** int
- **title :** varchar
- **address_id :** int (Clé étrangère vers le modèle Address)

