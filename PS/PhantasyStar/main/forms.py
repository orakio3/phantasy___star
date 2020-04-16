from django import forms
from .models import Game, Platform

class GameForm(forms.ModelForm):

    class Meta:
        model = Game
        fields = ['title', 'summary','release','platforms','faq','genre']


class PlatformForm(forms.ModelForm):

    class Meta:
        model = Platform
        fields = ['name','type']