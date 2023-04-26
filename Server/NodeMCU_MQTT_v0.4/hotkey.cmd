@echo off
doskey makemigrations = python manage.py makemigrations
doskey migrate = python manage.py migrate
doskey runserver = python manage.py runserver 0.0.0.0:8000