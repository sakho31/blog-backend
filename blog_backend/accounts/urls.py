from django.urls import path
from . import views
from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Accounts API"})

urlpatterns = [
    path('', home),
    path('auth/register/', views.register),
    path('auth/login/', views.login),
]