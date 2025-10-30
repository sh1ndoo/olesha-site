from django.contrib import admin

from .models import StreamItem, Game

admin.site.register(StreamItem)
admin.site.register(Game)