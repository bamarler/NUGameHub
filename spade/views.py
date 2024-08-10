from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserChangeForm
from django.contrib import messages
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
def account_view(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account was updated successfully!')
            return redirect('account')
    else:
        form = UserChangeForm(instance=request.user)
    
    return render(request, 'account.html', {'form': form})

def logout_view(request):
    auth_logout(request)
    return redirect('login_signup')  # Redirect to your combined login/signup view

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
