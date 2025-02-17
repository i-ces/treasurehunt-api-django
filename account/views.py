from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer
from rest_framework.permissions import AllowAny



# view for registering users
class RegisterView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        # Assuming you want to return some information or a form for registration
        return Response({"message": "GET request to register endpoint"})

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
