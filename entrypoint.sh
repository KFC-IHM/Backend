#!/bin/sh
python manage.py migrate
python manage.py init-admin
python manage.py runserver 0.0.0.0:8000