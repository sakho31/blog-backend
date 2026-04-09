from rest_framework import serializers
from .models import Amitie

class AmitieSerializer(serializers.ModelSerializer):
    nom      = serializers.CharField(source='receveur.nom',      read_only=True)
    username = serializers.CharField(source='receveur.username', read_only=True)

    class Meta:
        model  = Amitie
        fields = ['id', 'nom', 'username', 'statut', 'created_at']