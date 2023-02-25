#!/usr/bin/env bash

# This script is used to start the docker container
# shellcheck disable=SC2164
cd ./djangoapp
python manage.py makemigrations
echo -e "\e[34m >>> Migrating changes \e[97m"
python manage.py migrate
echo -e "\e[32m >>> migration completed \e[97m"
python manage.py runserver 0.0.0.0:8000