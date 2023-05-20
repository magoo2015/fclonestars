from django.urls import path
from . import views

urlpatterns = [
    path('', views.players_list),
    path('<int:pk>/', views.player_detail),
]