from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=20)
    score = models.IntegerField(default=0)
    password = models.CharField(max_length=30)
    photo = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"Team {self.name}"
