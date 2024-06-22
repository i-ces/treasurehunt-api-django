from django.contrib import admin

from .models import (
    Riddles,
)

class RiddleAdmin(admin.ModelAdmin):
    pass

admin.site.register(Riddles, RiddleAdmin)