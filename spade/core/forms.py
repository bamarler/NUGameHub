from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.text import slugify

from .models import Game

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Required. Enter a valid email address.")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove the "Password-based authentication" field if it exists
        if 'usable_password' in self.fields:
            del self.fields['usable_password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True, widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class GameUpdateForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['name', 'description', 'instructions', 'cover_image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'instructions': forms.Textarea(attrs={'rows': 3}),
        }
    
    def save(self, commit=True):
        game = super().save(commit=False)
        # Only update the slug if the name has changed
        if 'name' in self.changed_data:
            game.slug = slugify(game.name)
        if commit:
            game.save()
        return game