from django.db import models

from .level import Level

class Leaderboard(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE)

    score = models.PositiveIntegerField()
    rank = models.IntegerField()