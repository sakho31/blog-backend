from django.urls import path
from . import views

urlpatterns = [
    path('', views.articles),
    path('<int:pk>/', views.article_detail),  
]