from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from . models import Game, Platform
from .forms import GameForm, PlatformForm
from django.shortcuts import redirect

class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        games = Game.objects.all()
        context.update({
            'games': games
        })
        return context

class PlatformView(TemplateView):
    template_name = 'platform_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        platforms = Platform.objects.all()
        context.update({
            'platforms': platforms
        })
        return context



def game_detail(request, pk):
    game = get_object_or_404(Game, pk=pk)
    return render(request, 'main/game_detail.html', {'game': game})

def platform_detail(request, pk):
    platform = get_object_or_404(Platform, pk=pk)
    return render(request, 'main/platform_detail.html', {'platform': platform})



def forum(request):
    return render(request, 'main/forum.html', {'forum': forum})


def paypals(request):
    return render(request, 'main/pp.html', {'paypals': paypals})


def our_contacts(request):
    return render(request, 'main/contacts.html', {'contacts': our_contacts})


def new_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('game_detail', pk=post.pk)
    else:
        form = GameForm()
    return render(request, 'main/new_game.html', {'form': form })


def add_p(request):
    if request.method == 'POST':
        form = PlatformForm(request.POST)
    else:
        form = PlatformForm
    return render(request, 'main/add_p.html', {'form': form})














