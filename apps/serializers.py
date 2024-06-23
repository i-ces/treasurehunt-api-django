from rest_framework import serializers

from .models import Riddles, level, Team


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = level
        fields = ["number", "name"]


class RiddleSerializer(serializers.ModelSerializer):
    level = LevelSerializer

    class Meta:
        model = Riddles
        fields = ["riddle_id", "question", "is_available", "level"]


class TeamSerializer(serializers.Serializer):
    class Meta:
        fields = ["id", "name", "username", "score", "photo"]


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=30)
