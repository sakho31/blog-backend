# friends/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('',                      views.amis,                  name='amis'),
    path('request',               views.envoyer_demande,       name='envoyer-demande'),
    path('search/',               views.rechercher_utilisateur, name='rechercher'),
    path('<int:pk>/accept',       views.accepter_demande,      name='accepter-demande'),
    path('<int:pk>/block',        views.bloquer_ami,           name='bloquer-ami'),
    path('<int:pk>',              views.supprimer_ami,         name='supprimer-ami'),
]