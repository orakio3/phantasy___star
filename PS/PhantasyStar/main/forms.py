from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Game, Platform


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'summary', 'release', 'platforms', 'faq', 'genre', 'image']


class PlatformForm(forms.ModelForm):

    class Meta:
        model = Platform
        fields = ['name', 'type']


class RegForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'password1',
            'password2',
            'email',
        )
    def save(self, commit=True):
        user = super(RegForm, self).save(commit=False)
        user.first_name =self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user