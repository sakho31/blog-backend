from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Amitie(models.Model):
    STATUT_CHOICES = [
        ('en_attente', 'En attente'),
        ('accepte',    'Accepté'),
        ('bloque',     'Bloqué'),
    ]

    demandeur  = models.ForeignKey(User, on_delete=models.CASCADE, related_name='demandes_envoyees')
    receveur   = models.ForeignKey(User, on_delete=models.CASCADE, related_name='demandes_recues')
    statut     = models.CharField(max_length=20, choices=STATUT_CHOICES, default='en_attente')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Un utilisateur ne peut envoyer qu'une seule demande à un autre
        unique_together = ('demandeur', 'receveur')

    def __str__(self):
        return f"{self.demandeur} → {self.receveur} ({self.statut})"
