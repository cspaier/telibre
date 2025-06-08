# telibre

## Déploiement local

- Créer un environnement virtuel python: `python -m venv venv`
- L'activer: `source venv/bin/activate`
- Installer les dépendances: `pip install -r requirements.txt`
- Appliquer les migrations `./manage.py migrate`
- Installer les données initiales `./manage.py loaddata initial.json`
- Lancer le serveur `./manage.py runserver`

Vous pouvez vous connecter sur [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) avec les identifiants admin/admin.

