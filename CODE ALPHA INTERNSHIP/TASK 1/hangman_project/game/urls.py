from django.urls import path
from . import views

urlpatterns = [
    path('', views.hangman, name='hangman'),
    path('reset/', views.reset_game, name='reset_game'),
]
