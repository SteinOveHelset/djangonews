from django.contrib import admin

from .models import Story, Comment, Vote

admin.site.register(Story)
admin.site.register(Comment)
admin.site.register(Vote)