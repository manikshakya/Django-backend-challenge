from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('addBook/', views.addBook),
    path('searchBook/', views.searchBook),
    path('searchVocabulary/', views.searchVocabulary),
    path('addVocabulary/', views.addVocabulary),
]
