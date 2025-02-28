# SalesPageApp

SalesPageApp est une application web Django containerisée avec Docker et déployée en production via Nginx et PostgreSQL.

## 🚀 Installation & Configuration

### 1️⃣ Prérequis
Assurez-vous d'avoir installé :
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Pipenv](https://pipenv.pypa.io/en/latest/)

---

## ⚙️ Lancement en Développement

1. **Cloner le dépôt** :
```sh
 git clone https://github.com/ton-utilisateur/salespageapp.git
 cd salespageapp
```

2. **Créer et configurer l'environnement** :
   - Copier le fichier `.env.example` et le renommer en `.env`.
   - Remplir les variables avec les bonnes valeurs.

3. **Lancer l'application en mode développement** :
```sh
 docker-compose up --build
```

4. **Accéder à l'application** :
   - Django : `http://127.0.0.1:8000`
   - Admin Panel : `http://127.0.0.1:8000/admin`
   - Base de données PostgreSQL tourne sur `localhost:5432`.

5. **Exécuter les migrations et créer un superutilisateur** :
```sh
docker-compose exec web pipenv run python manage.py migrate
docker-compose exec web pipenv run python manage.py createsuperuser
```

---

## 🏗️ Lancement en Production

1. **Créer les fichiers d'environnement** :
   - Copier `.env.example` en `.env.prod` et `.env.prod.db`.
   - Remplir les valeurs correctement.

2. **Construire et lancer les containers** :
```sh
docker-compose -f docker-compose.prod.yml up --build -d
```

3. **Collecter les fichiers statiques** :
    - Normalement, entrypoint.sh s'occupe de collecter mes fichiers static, mais ce dernier ne fonctionnant pas, j'ai dû copier coller manuellement mes fichiers avec :
```sh
cp -r /usr/src/salesPageApp/app/static/* /usr/src/salesPageApp/app/staticfiles
```

4. **Accéder à l'application** :
   - Application : `http://127.0.0.1:1337`
   - Admin Panel : `http://127.0.0.1:1337/admin`

---

## 🛠️ Commandes Utiles

**Voir les logs d'un service spécifique** :
```sh
docker-compose logs -f web  # Pour Django
docker-compose logs -f db   # Pour PostgreSQL
docker-compose logs -f nginx # Pour Nginx
```

**Arrêter les containers** :
```sh
docker-compose down
```

**Supprimer tous les containers, volumes et réseaux associés** :
```sh
docker-compose down -v
```

---

## 📌 Stack Utilisée
- **Django** - Framework backend
- **Bootstrap** - Framework CSS
- **Gunicorn** - Serveur d'application WSGI
- **PostgreSQL** - Base de données
- **Docker & Docker Compose** - Conteneurisation
- **Nginx** - Proxy inverse pour la production

---

## 💡 Contributions
Les contributions sont les bienvenues ! N’hésitez pas à proposer des améliorations via une PR.

🔥 Bon développement !

