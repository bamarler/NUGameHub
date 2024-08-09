from django.shortcuts import render
from .models import Game

def home(request):
    return render(request, 'home.html')

def account_page(request):
    return render(request, 'account.html')

def leaderboards(request):
    return render(request, 'leaderboards.html')

def social(request):
    return render(request, 'social.html')

def catalog(request):
    games = Game.objects.all()
    return render(request, 'catalog.html', {'games': games})

def game_view(request, game_id):
    game = Game.objects.get(pk=game_id)
    return render(request, 'game_template.html', {'game': game})
