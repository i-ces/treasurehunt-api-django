from django.contrib import admin

from .models import (
    Riddles,
    Level,
)

class RiddleAdmin(admin.ModelAdmin):
    pass

admin.site.register(Riddles, RiddleAdmin)
admin.site.register(Level)