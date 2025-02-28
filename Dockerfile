# Dockerfile pour Django
FROM python:3.13-slim

# Définir le répertoire de travail
WORKDIR /usr/src/salesPageApp

# Copier les fichiers de l'application
COPY ./app ./app
COPY Pipfile .
COPY Pipfile.lock .

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

RUN mkdir /usr/src/salesPageApp/app/staticfiles
RUN mkdir /usr/src/salesPageApp/app/mediafiles

WORKDIR /usr/src/salesPageApp/app

# Exposer le port 8000
EXPOSE 8000

ENTRYPOINT ["/usr/src/salesPageApp/entrypoint.sh"]