from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template.context_processors import request
from django.views import generic
from django.views.generic import TemplateView
from . models import Game, Platform
from .forms import GameForm, PlatformForm, RegForm
from django.shortcuts import redirect



def HomeView(request):
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    return render(request, 'home_page.html', context={'num_visits': num_visits})


class GamesView(generic.ListView):
    model = Game
    paginate_by = 8


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


def add_g(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            game = form.save()
            game.save()
            return redirect('game_detail', pk = game.pk)
    else:
        form = GameForm
    return render(request, 'main/new_game.html', {'form': form})


def add_p(request):
    if request.method == 'POST':
        form = PlatformForm(request.POST)
    else:
        form = PlatformForm
    return render(request, 'main/add_p.html', {'form': form})


                            #REGISTRATION VIEWS

def register(request):
    form_class = RegForm
    form = form_class(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/main')
        else:
            return HttpResponse('Куда ты нахуй ломишься?!', status_code=400)
    return render(request, 'registration/reg_form.html', {'form': form})













