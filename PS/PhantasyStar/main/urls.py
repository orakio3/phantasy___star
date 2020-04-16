from django.urls import path
from . import views
from . views import HomeView


urlpatterns = [
    path('', HomeView.as_view(), name= 'index'),
    path('platforms/', views.PlatformView.as_view(), name='platforms'),
    path('<int:pk>/', views.game_detail, name='game_detail'),
    path('platforms/<int:pk>/', views.platform_detail, name='platform_detail'),
    path('forum/', views.forum, name='forum'),
    path('pp/', views.paypals, name='pp'),
    path('our_contacts/', views.our_contacts, name='contacts'),
    path('new_game/', views.new_game, name='new_game'),
    path('add_platform/', views.add_p, name='add_p'),
]