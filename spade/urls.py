"""
URL configuration for SPADE.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('catalog/', views.catalog, name='catalog'),
    path('catalog/<int:game_id>/', views.game_view, name='game_view'),
    path('leaderboards/', views.leaderboards, name='leaderboards'),
    path('social/', views.social, name='social'),
    path('account/', views.account_page, name='account_page'),
    # Combined login/signup view
    path('login/', views.login_signup, name='login_signup'),
    # These are needed for the login view to function properly
    path('auth_login/', auth_views.LoginView.as_view(), name='login'),  # Default Django login view
    path('auth_signup/', views.login_signup, name='signup'),  # Your custom signup view
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
