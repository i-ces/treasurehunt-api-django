from django.db import models

from .riddles import Riddles

class Leaderboard(models.Model):
    level = models.ForeignKey(Riddles)

    score = models.DecimalField()