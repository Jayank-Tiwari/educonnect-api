#!/usr/bin/env bash
set -e

echo "[startup] Checking for Django project..."
if [ ! -f manage.py ]; then
  echo "[startup] No manage.py found. Creating Django project 'educonnect'..."
  django-admin startproject educonnect .
  echo "[startup] Project created."
fi

echo "[startup] Running server..."
python manage.py runserver 0.0.0.0:8000