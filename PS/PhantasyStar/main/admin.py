from django.contrib import admin
from . models import Game, Platform, Genre, New


admin.site.register(Game)
admin.site.register(Platform)
admin.site.register(Genre)
admin.site.register(New)

