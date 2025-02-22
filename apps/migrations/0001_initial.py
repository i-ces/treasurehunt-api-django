# Generated by Django 4.2.10 on 2024-06-22 11:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Level",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("number", models.IntegerField(unique=True)),
                ("name", models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name="Riddles",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("riddle_id", models.IntegerField()),
                ("question", models.TextField()),
                ("answer", models.CharField(max_length=200)),
                ("is_available", models.BooleanField(default=True)),
                ("is_trap", models.BooleanField(default=True)),
                (
                    "level",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="apps.level"
                    ),
                ),
            ],
        ),
    ]
