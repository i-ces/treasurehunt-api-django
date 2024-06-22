from django.contrib import admin

from .models import (
    Riddles,
    Level,
)

admin.site.register(Riddles)
admin.site.register(Level)