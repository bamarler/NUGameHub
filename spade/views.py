from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from .models import Game

def login_signup(request):
    login_form = AuthenticationForm()
    signup_form = CustomUserCreationForm()
    return render(request, 'login_signup.html', {'login_form': login_form, 'signup_form': signup_form})

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def account_page(request):
    return render(request, 'account.html')

@login_required
def leaderboards(request):
    return render(request, 'leaderboards.html')

@login_required
def social(request):
    return render(request, 'social.html')

@login_required
def catalog(request):
    games = Game.objects.all()
    return render(request, 'catalog.html', {'games': games})

@login_required
def game_view(request, game_id):
    game = Game.objects.get(pk=game_id)
    return render(request, 'game_template.html', {'game': game})
