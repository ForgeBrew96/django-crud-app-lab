from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('games/', views.game_index, name='game-index'),
    path('about/', views.board, name='about')
]