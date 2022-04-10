from django.shortcuts import render
from django.shortcuts import redirect
from . import models

# Create your views here.
def choose_character(request):
    character = request.session.get("character")
    if request.method == "POST":
        # create a new player and enter the game
        return render(request, 'game/game.html', locals())
    return render(request, 'game/index.html', locals())


def game(request):
    return render(request, 'game/game.html', locals())