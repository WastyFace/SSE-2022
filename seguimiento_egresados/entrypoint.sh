#!/bin/sh
su -c 'python3 manage.py makemigrations'
su -c 'python3 manage.py migrate'
su -c 'gunicorn --bind :8000 seguimiento_egresados.wsgi:application --reload'