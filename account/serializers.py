from rest_framework import serializers
from .models import UserData

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserData
        fields = ["id", "username", "name", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        print(validated_data)  # Debugging line to check validated data
        username = validated_data.get("username")
        name = validated_data.get("name")
        password = validated_data.get("password")
        
        user = UserData.objects.create_user(
            username=username,
            name=name,
            password=password
        )
        return user
