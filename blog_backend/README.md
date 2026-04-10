# Blog Personnel — Backend Django

API REST développée avec Django et Django REST Framework pour le projet de blog personnel

## Technologies utilisées

- **Django 6.0.4**
- **Django REST Framework** — création de l'API REST
- **Simple JWT** — authentification par token JWT
- **django-cors-headers** — communication avec le frontend React
- **PostgreSQL** — base de données

## Fonctionnalités de l'API

- Inscription et connexion avec génération de token JWT
- CRUD complet sur les articles
- Gestion des amitiés (demande, acceptation, blocage, suppression)
- Recherche d'utilisateurs par username
- Filtrage des articles selon les relations d'amitié

## Structure du projet

```
blog_backend/
├── accounts/
│   ├── models.py        # Modèle User personnalisé
│   ├── serializers.py   # Sérialisation des données utilisateur
│   ├── views.py         # Vues register et login
│   └── urls.py          # Routes authentification
├── articles/
│   ├── models.py        # Modèle Article
│   ├── serializers.py   # Sérialisation des articles
│   ├── views.py         # Vues CRUD articles
│   └── urls.py          # Routes articles
├── friends/
│   ├── models.py        # Modèle Amitie
│   ├── serializers.py   # Sérialisation des amitiés
│   ├── views.py         # Vues gestion des amis
│   └── urls.py          # Routes amis
└── blog_backend/
    ├── settings.py      # Configuration Django
    └── urls.py          # Routes principales
```

## Installation et lancement

### Prérequis
- Python 3.12+
- PostgreSQL installé et configuré

### Étapes

```bash
# Cloner le dépôt
git clone https://github.com/TON_USERNAME/blog-backend.git
cd blog-backend/blog_backend

# Créer et activer l'environnement virtuel
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Installer les dépendances
pip install django djangorestframework django-cors-headers djangorestframework-simplejwt python-dotenv

# Configurer les variables d'environnement
# Modifier .env avec vos informations

# Appliquer les migrations
python manage.py makemigrations
python manage.py migrate

# Lancer le serveur
python manage.py runserver
```

L'API sera accessible sur `http://localhost:8000`

## Variables d'environnement

Créez un fichier `.env` à la racine du projet `blog_backend/` :

```env
SECRET_KEY=votre_cle_secrete_django
DEBUG=True
DB_NAME=blog_db
DB_USER=votre_utilisateur_postgres
DB_PASSWORD=votre_mot_de_passe
DB_HOST=localhost
DB_PORT=5432
```

## Endpoints de l'API

### Authentification

| Méthode | URL | Description | Accès |
|---------|-----|-------------|-------|
| POST | `/api/accounts/auth/register/` | Inscription | Public |
| POST | `/api/accounts/auth/login/` | Connexion | Public |

### Articles

| Méthode | URL | Description | Accès |
|---------|-----|-------------|-------|
| GET | `/api/articles/` | Liste des articles | Connecté |
| POST | `/api/articles/` | Créer un article | Connecté |
| PUT | `/api/articles/<id>/` | Modifier un article | Auteur |
| DELETE | `/api/articles/<id>/` | Supprimer un article | Auteur |

### Amis

| Méthode | URL | Description | Accès |
|---------|-----|-------------|-------|
| GET | `/api/friends/` | Liste des amis | Connecté |
| POST | `/api/friends/request` | Envoyer une demande | Connecté |
| GET | `/api/friends/search/` | Rechercher un utilisateur | Connecté |
| PATCH | `/api/friends/<id>/accept` | Accepter une demande | Connecté |
| PATCH | `/api/friends/<id>/block` | Bloquer un ami | Connecté |
| DELETE | `/api/friends/<id>` | Supprimer un ami | Connecté |

## Modèles de données

### User
```
id, nom, username, password
```

### Article
```
id, titre, contenu, est_public, commentaires_actifs, auteur, created_at, updated_at
```

### Amitie
```
id, demandeur, receveur, statut (en_attente/accepte/bloque), created_at
```

