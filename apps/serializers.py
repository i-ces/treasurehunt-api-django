from rest_framework import serializers

from .models import Riddles, Team, UserProgress, Level


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
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


class UserProgressSerializer(serializers.ModelSerializer):
    solved_riddles = RiddleSerializer(many=True, read_only=True)

    class Meta:
        model = UserProgress
        fields = ("current_level", "solved_riddles")
