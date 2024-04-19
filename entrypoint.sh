#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $DATABASE_HOST $DATABASE_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py flush --no-input
python manage.py migrate
#python manage.py loaddata categories.json
#python manage.py loaddata projects.json
#python manage.py loaddata contact_info.json

python manage.py test themes.tests.ThemeTest

if [ "$DEBUG" = "False" ]
then
    python manage.py collectstatic --noinput
fi

if [ "$DJANGO_SUPERUSER_USERNAME" ]
then
    python manage.py createsuperuser \
        --noinput \
        --username $DJANGO_SUPERUSER_USERNAME \
        --email $DJANGO_SUPERUSER_EMAIL \
        --first_name $DJANGO_SUPERUSER_FIRST_NAME \
        --last_name $DJANGO_SUPERUSER_LAST_NAME
fi

exec "$@"
