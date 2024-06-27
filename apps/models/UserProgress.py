from django.contrib.auth import get_user_model
from django.db import models

from .level import Level
from .riddles import Riddles

User = get_user_model()


class UserProgress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="progress")
    current_level = models.ForeignKey(
        Level, on_delete=models.SET_NULL, null=True, blank=True
    )
    solved_riddle = models.ManyToManyField(Riddles, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Progress for {self.user.email}"
