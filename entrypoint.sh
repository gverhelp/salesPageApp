#!/bin/sh

# Vider la base de données
# pipenv run python manage.py flush --no-input

# Appliquer les migrations
pipenv run python manage.py migrate

# Collecter les fichiers statiques
pipenv run python manage.py collectstatic --no-input --clear
cp -r /usr/src/salesPageApp/app/static/* /usr/src/salesPageApp/app/staticfiles #Added this because collectstatic was not working for some reason

# Créer le superutilisateur si les variables d'environnement sont définies
if [ "$DJANGO_SUPERUSER_USERNAME" ] && [ "$DJANGO_SUPERUSER_EMAIL" ] && [ "$DJANGO_SUPERUSER_PASSWORD" ]
then
    echo "Creating superuser..."
    pipenv run python manage.py createsuperuser --noinput \
    --username $DJANGO_SUPERUSER_USERNAME \
    --email $DJANGO_SUPERUSER_EMAIL

    echo "from django.contrib.auth.models import User; user = User.objects.get(username='$DJANGO_SUPERUSER_USERNAME'); user.set_password('$DJANGO_SUPERUSER_PASSWORD'); user.save()" | pipenv run python manage.py shell
else
    echo "Superuser not created because required environment variables are not set."
fi

# Exécuter la commande passée en argument
exec "$@"

