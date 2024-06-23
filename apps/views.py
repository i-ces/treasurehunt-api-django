from .models import Riddles, Team
from .serializers import LoginSerializer, RiddleSerializer
from apps.helper import get_tokens_for_user
from django.contrib.auth import authenticate
from .models import Riddles
from .serializers import RiddleSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action


class RiddleViewSet(viewsets.ModelViewSet):
    queryset = Riddles.objects.all()
    serializer_class = RiddleSerializer
    lookup_field = 'riddle_id'
    http_method_names = ['get', 'head', 'options']

    def retrive(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @action(detail=True, methods=['get'], url_path='verify')
    def validate_answer(self, request, riddle_id=None):
        answer = request.query_params.get('answer')
        riddle = self.get_object()

        if answer is None:
            return Response({"detail": "Answer query parameter is required"}, status=400)
        if riddle.answer.lower() == answer.lower() and riddle.is_trap == False:
            return Response({"detail": "Correct Answer!"}, status=200)
        else:
            print(riddle.is_trap)
            if riddle.is_trap:
                level = riddle.level
                level.trap_count += 1
                level.save()

                if level.trap_count > 2:
                    Riddles.objects.filter(level=level, is_trap=True).update(is_available=False)
                    return Response({"detail": "This was a Trap. All traps for this level are now unavailable. Try again!"}, status=400)

            return Response({"detail": "This was a trap try again"}, status= 400)


class RiddleByLevelAPIView(viewsets.ModelViewSet):
    serializer_class = RiddleSerializer
    http_method_names = ['get', 'options']

    def get_queryset(self):
        level = self.kwargs.get('level')
        return Riddles.objects.filter(level=level, is_available=True)

class LoginApiView(viewsets.ViewSet):
    @action(detail=False, methods=['post'], url_path=None)
    def login(self, request):
        data = request.data
        serializer = LoginSerializer(data=data)
        # check for input validation
        if serializer.is_valid():
            username = serializer.data.get('username')
            password = serializer.data.get('password')
            print(f"username: {username}, password: {password}")
            # try to authenticate
            # user = authenticate(username=username, password=password)
            # print(f"user: {user}")
            user = Team.objects.filter(
                username=username, password=password).first()
            print("user type: ", type(user))
            print(f"user_t: {user}")
            # check if user is authenticated
            if user is None:
                return Response({"message": "Invalid credentials"}, status=401)
            # if user is authenticated
            return Response(get_tokens_for_user(user))
        return Response({"message": "Invalid input"}, status=400)
