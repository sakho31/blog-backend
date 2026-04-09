from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Q
from django.contrib.auth import get_user_model

from .models import Amitie
from .serializers import AmitieSerializer

User = get_user_model()


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def amis(request):

    relations = Amitie.objects.filter(
        Q(demandeur=request.user) | Q(receveur=request.user)
    )

    serializer = AmitieSerializer(relations, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def envoyer_demande(request):

    user_id = request.data.get('user_id')

    try:
        receveur = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response({'error': 'Utilisateur introuvable'}, status=404)

    if receveur == request.user:
        return Response({'error': 'Impossible de s’ajouter soi-même'}, status=400)

    amitie, created = Amitie.objects.get_or_create(
        demandeur=request.user,
        receveur=receveur
    )

    return Response(
        AmitieSerializer(amitie).data,
        status=201 if created else 200
    )


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def accepter_demande(request, pk):

    try:
        amitie = Amitie.objects.get(pk=pk, receveur=request.user)
        amitie.statut = 'accepte'
        amitie.save()

        return Response(AmitieSerializer(amitie).data)

    except Amitie.DoesNotExist:
        return Response({'error': 'Demande introuvable'}, status=404)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def bloquer_ami(request, pk):

    try:
        amitie = Amitie.objects.get(
            Q(demandeur=request.user) | Q(receveur=request.user),
            pk=pk
        )

        amitie.statut = 'bloque'
        amitie.save()

        return Response(AmitieSerializer(amitie).data)

    except Amitie.DoesNotExist:
        return Response({'error': 'Relation introuvable'}, status=404)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def supprimer_ami(request, pk):

    try:
        amitie = Amitie.objects.get(
            Q(demandeur=request.user) | Q(receveur=request.user),
            pk=pk
        )

        amitie.delete()
        return Response(status=204)

    except Amitie.DoesNotExist:
        return Response({'error': 'Relation introuvable'}, status=404)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def rechercher_utilisateur(request):

    username = request.query_params.get('username', '')

    try:
        user = User.objects.get(username=username)
        return Response({
            'id': user.id,
            'username': user.username
        })

    except User.DoesNotExist:
        return Response({'error': 'Utilisateur introuvable'}, status=404)
