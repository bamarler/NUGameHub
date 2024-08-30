from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import get_object_or_404
from django.core.files.base import ContentFile
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Game
from .forms import CustomUserCreationForm
from .forms import UserUpdateForm
from .forms import GameUpdateForm
from .forms import GameCodeForm

def login_signup(request):
    if request.method == 'POST':
        if 'login' in request.POST:
            login_form = AuthenticationForm(data=request.POST)
            signup_form = CustomUserCreationForm()
            if login_form.is_valid():
                login(request, login_form.get_user())
                return redirect('home')
            else:
                return render(request, 'login_signup.html', {'login_form': login_form, 'signup_form': signup_form, 'active_tab': 'login'})

        elif 'signup' in request.POST:
            signup_form = CustomUserCreationForm(request.POST)
            login_form = AuthenticationForm()
            if signup_form.is_valid():
                user = signup_form.save()
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'login_signup.html', {'login_form': login_form, 'signup_form': signup_form, 'active_tab': 'signup'})
    else:
        login_form = AuthenticationForm()
        signup_form = CustomUserCreationForm()
        return render(request, 'login_signup.html', {'login_form': login_form, 'signup_form': signup_form, 'active_tab': 'login'})

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def account_view(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account information has been updated successfully.')
            return redirect('account')  # Replace 'account' with your URL name for the account page
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = UserUpdateForm(instance=request.user)
    
    context = {
        'form': form
    }
    return render(request, 'account.html', context)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important! Keeps the user logged in.
            messages.success(request, 'Your password was successfully updated!')
            return redirect('account')  # Redirect to the account page
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'password_change.html', {
        'form': form
    })

def logout_view(request):
    auth_logout(request)
    return redirect('login_signup')  # Redirect to your combined login/signup view

@login_required
def catalog(request):
    games = Game.objects.all()
    return render(request, 'catalog.html', {'games': games})

@login_required
def game_view(request, slug):
    game = get_object_or_404(Game, slug=slug)
    return render(request, 'game_template.html', {'game': game})

@login_required
def leaderboards(request):
    return render(request, 'leaderboards.html')

@login_required
@user_passes_test(lambda u: u.is_staff)
def develop(request):
    games = Game.objects.filter(developer=request.user.username)
    return render(request, 'develop.html', {'games': games})

@login_required
@user_passes_test(lambda u: u.is_staff)
def develop_game(request, slug):
    game = get_object_or_404(Game, slug=slug)

    if request.method == 'POST':
        form = GameUpdateForm(request.POST, request.FILES, instance=game)
        if form.is_valid():
            form.save()
            return redirect('develop_game', slug=game.slug)
    else:
        form = GameUpdateForm(instance=game)

    return render(request, 'develop_game.html', {'game': game, 'form': form})

@login_required
@user_passes_test(lambda u: u.is_staff)
def create_game(request):
    if request.method == 'POST':
        game_name = request.POST.get('game_name', 'Untitled Game')
        template_js_path = request.POST.get('template_js_path')
        
        # Create the new game object
        game = Game.objects.create(
            name=game_name,
            developer=request.user.username,
            status='developing'
        )
        
        # Set the JS file field
        #game.js_file.save(f'{game.slug}.js', ContentFile(open(template_js_path, 'rb').read()))
        game.js_file.save(f'{game.slug}.js', ContentFile(f'// {game_name}'))

        # Redirect to the develop page
        return redirect('develop')

@login_required
@user_passes_test(lambda u: u.is_staff)
@csrf_exempt
def save_game_js(request, slug):
    if request.method == 'POST':
        try:
            game = Game.objects.get(slug=slug)
            print(game)
            data = json.loads(request.body.decode('utf-8'))
            code = data.get('code')

            if code:
                form = GameCodeForm(instance=game)
                form.save_js_code(code)
                return JsonResponse({'status': 'success'})
            return JsonResponse({'status': 'fail', 'message': 'No code provided'}, status=400)
        except Game.DoesNotExist:
            return JsonResponse({'status': 'fail', 'message': 'Game not found'}, status=404)
        except Exception as e:
            return JsonResponse({'status': 'fail', 'message': str(e)}, status=500)
    return JsonResponse({'status': 'fail', 'message': 'Invalid request method'}, status=405)

@login_required
def social(request):
    return render(request, 'social.html')


