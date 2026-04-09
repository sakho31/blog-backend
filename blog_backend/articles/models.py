from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Article(models.Model):
    titre               = models.CharField(max_length=200)
    contenu             = models.TextField()
    est_public          = models.BooleanField(default=True)
    commentaires_actifs = models.BooleanField(default=True)
    auteur              = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titre