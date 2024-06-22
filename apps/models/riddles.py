from django.db import models

from .level import Level

class Riddles(models.Model):
    riddle_id = models.IntegerField()
    question = models.TextField()
    answer = models.CharField(max_length=200)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)
    is_trap = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.question} {self.riddle_id} (Level {self.level.number})"
