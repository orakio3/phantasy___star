from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from . import views
from .views import GamesView

urlpatterns = [
    path('', views.HomeView, name='index'),
    path('games/', GamesView.as_view(), name='games'),
    path('platforms/', views.PlatformView.as_view(), name='platforms'),
    path('<int:pk>/', views.game_detail, name='game_detail'),
    path('platforms/<int:pk>/', views.platform_detail, name='platform_detail'),
    path('forum/', views.forum, name='forum'),
    path('pp/', views.paypals, name='pp'),
    path('our_contacts/', views.our_contacts, name='contacts'),
    path('new_game/', views.add_g, name='add_g'),
    path('add_platform/', views.add_p, name='add_p'),
    path('login/', LoginView.as_view(), {'template_name': 'registration/login.html'}, name='login'),
    path('logout/', LogoutView.as_view(), {'template_name': 'registration/logout.html'}, name='logout'),
    path('register/', views.register, name='register'),
]

