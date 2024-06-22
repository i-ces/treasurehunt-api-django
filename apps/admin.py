from django.contrib import admin

from .models import (
    Riddles,
    Level,
    Team,
)


class RiddleAdmin(admin.ModelAdmin):
    pass


admin.site.register(Riddles, RiddleAdmin)
admin.site.register(Level)
admin.site.register(Team)
