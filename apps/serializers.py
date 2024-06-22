from rest_framework import serializers

from .models import Riddles


class RiddleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Riddles
        fields = ["id", "question", "is_available"]
