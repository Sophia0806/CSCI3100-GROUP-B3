from django.urls import path
from . import views
urlpatterns = [
    path('character/', views.choose_character, name='choose_character'),
    path('game/', views.game, name='game'),
]
