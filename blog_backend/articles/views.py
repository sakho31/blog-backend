from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Q
from .models import Article
from .serializers import ArticleSerializer
from friends.models import Amitie

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def articles(request):
    if request.method == 'GET':
        relations_acceptees = Amitie.objects.filter(
            Q(demandeur=request.user) | Q(receveur=request.user),
            statut='accepte'
        )
        relations_bloquees = Amitie.objects.filter(
            Q(demandeur=request.user) | Q(receveur=request.user),
            statut='bloque'
        )
        amis_ids = set()
        for r in relations_acceptees:
            amis_ids.add(r.demandeur_id)
            amis_ids.add(r.receveur_id)
        amis_ids.discard(request.user.id)
        bloques_ids = set()
        for r in relations_bloquees:
            bloques_ids.add(r.demandeur_id)
            bloques_ids.add(r.receveur_id)
        bloques_ids.discard(request.user.id)
        amis_ids = amis_ids - bloques_ids
        mes_articles = Article.objects.filter(auteur=request.user)
        articles_amis = Article.objects.filter(
            auteur_id__in=amis_ids,
            est_public=True
        )

        articles_total = (mes_articles | articles_amis).order_by('-created_at')
        serializer = ArticleSerializer(articles_total, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(auteur=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def article_detail(request, pk):
    try:
        article = Article.objects.get(pk=pk, auteur=request.user)
    except Article.DoesNotExist:
        return Response({'error': 'Article introuvable'}, status=404)

    if request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=204)