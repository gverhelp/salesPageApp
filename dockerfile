# Dockerfile pour Django
FROM python:3.13

# Définir le répertoire de travail
WORKDIR /usr/src/salesPageApp

# Copier les fichiers de l'application
COPY . .

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Installer Pipenv et les dépendances
RUN pip install --upgrade pip \
    && pip install pipenv \
    && pipenv install --deploy --ignore-pipfile

RUN chmod +x /usr/src/salesPageApp/entrypoint.sh

WORKDIR /usr/src/salesPageApp/app

# Exposer le port 8000
EXPOSE 8000

# Lancer l'application
# CMD ["pipenv", "run", "gunicorn", "salesPageApp.wsgi:application", "--bind", "0.0.0.0:8000"]
# CMD ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
ENTRYPOINT ["sh", "/usr/src/salesPageApp/entrypoint.sh"]
