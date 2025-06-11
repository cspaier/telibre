# telibre

Un projet django avec:

- [wagtail](https://wagtail.org/) comme CMS
- [django allauth](https://docs.allauth.org/en/latest/) comme gestionnaire d'authentification
- [django cotton](https://django-cotton.com/) pour les composants basés sur [daisy ui](https://daisyui.com/).


## Déploiement local

- Créer un environnement virtuel python: `python -m venv venv`
- L'activer: `source venv/bin/activate`
- Installer les dépendances: `pip install -r requirements.txt`
- Appliquer les migrations `./manage.py migrate`
- Installer les données initiales `./manage.py loaddata initial.json`
- Installer les dépendances front `./manage.py tailwind install`
- Lancer le serveur `./manage.py runserver_watch`

Vous pouvez vous connecter sur [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) avec les identifiants admin/admin.

## Côté front
On utilise [django-tailwind](https://django-tailwind.readthedocs.io/en/latest/) qui fournit une intégration simple de django, tailwind, postcss. On a ajouté les dépendances [daisyui](https://daisyui.com/) et [tailwindcss-typography](https://tailwindcss-typography.vercel.app/).

La gestion des dépendances et configurations node se trouve dans le dossier `theme/static_src`.

Pour installer les dépendances node, `./manage.py tailwind install` à la racine lancera `npm install` dans le dossier `/theme/static_src`.

L'application `theme` fournit également une commande django `runserver_watch` qui lance dans deux processus:
- `./manage.py runserver` : lance le serveur django
- `./manage.py tailwind watch`: lance `npm start` qui surveille les fichiers statiques afin de recharger le navigateur au changement.

## Organisation

- `telibre` contient les reglages et templates généraux.
- `home` contient les modèles et templates pour wagtail.
- `address` gère les adresses des utilisateus.