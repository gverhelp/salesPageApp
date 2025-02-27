# Dockerfile pour Django
FROM python:3.13-slim

# Définir le répertoire de travail
WORKDIR /usr/src/salesPageApp

# Copier les fichiers de l'application
COPY ./app ./app
COPY Pipfile .
COPY Pipfile.lock .
COPY .env .

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Installer Pipenv et les dépendances
RUN pip install --upgrade pip \
    && pip install pipenv \
    && pipenv install --deploy --ignore-pipfile

COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/salesPageApp/entrypoint.sh
RUN chmod +x /usr/src/salesPageApp/entrypoint.sh

WORKDIR /usr/src/salesPageApp/app

# Exposer le port 8000
EXPOSE 8000

ENTRYPOINT ["sh", "/usr/src/salesPageApp/entrypoint.sh"]

# Lancer l'application
# CMD ["pipenv", "run", "gunicorn", "salesPageApp.wsgi:application", "--bind", "0.0.0.0:8000"]
# CMD ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]

