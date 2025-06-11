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
- Lancer le serveur `./manage.py runserver`

Vous pouvez vous connecter sur [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) avec les identifiants admin/admin.

