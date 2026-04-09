from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    auteur_nom = serializers.CharField(source='auteur.nom', read_only=True)
    auteur_id  = serializers.IntegerField(source='auteur.id', read_only=True)

    class Meta:
        model  = Article
        fields = [
            'id', 'titre', 'contenu', 'est_public',
            'commentaires_actifs',
            'auteur',          
            'auteur_id',
            'auteur_nom',
            'created_at'
        ]
        read_only_fields = ['auteur']  