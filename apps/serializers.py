from rest_framework import serializers

from .models import Riddles,level

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model=level
        fields = ["number", "name"]

class RiddleSerializer(serializers.ModelSerializer):
    level = LevelSerializer

    class Meta:
        model = Riddles
        fields = ["riddle_id", "question", "is_available", "level"]
