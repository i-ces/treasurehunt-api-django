from django.db import models


class Level(models.Model):
    number = models.IntegerField(unique=True)
    name = models.CharField(max_length=500)
    trap_count = models.IntegerField(default=0)

    def __str__(self):
        return f"Level {self.number}: {self.name}"
