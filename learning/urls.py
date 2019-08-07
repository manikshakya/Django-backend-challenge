from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('addBook/', views.addBook),
    path('searchBook/', views.searchBook),
    path('searchVocabulary/', views.searchVocabulary),
    path('addVocabulary/', views.addVocabulary),

    path('searchBook/json1/', views.Json1.as_view()),
    path('searchVocabulary/json2/', views.Json2.as_view()),
]
