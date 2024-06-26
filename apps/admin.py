from django.contrib import admin

from .models import Level, Riddles, Team

admin.site.register(Riddles)
admin.site.register(Level)
admin.site.register(Team)
