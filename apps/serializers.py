from rest_framework import serializers

from .models import Riddles, Team


class RiddleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Riddles
        fields = ["id", "question", "is_available"]


class TeamSerializer(serializers.Serializer):
    class Meta:
        model = Team
        fields = ["id", "name", "username", "score", "photo"]
