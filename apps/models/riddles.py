from django.db import models

class Riddles(models.Model):
    LEVEL_CHOICES=[
        (1, 'level 1'),
        (2, 'level 2'),
        (3, 'level 3'),
        (4, 'level 4'),
        (5, 'level 5'),
        (6, 'level 6'),
        (7, 'level 7'),
        (8, 'level 8'),
        (9, 'level 9'),
        (10, 'level 10'),
    ]

    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=200)
    level = models.IntegerField(choices=LEVEL_CHOICES)

    def __dtr__(self):
        return f"{self.question} (Level {self.level})"

