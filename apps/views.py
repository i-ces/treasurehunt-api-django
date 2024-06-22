from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import RiddleSerializer
from .models import Riddles

class RiddleViewSet(viewsets.ModelViewSet):
    queryset = Riddles.objects.all()
    serializer_class = RiddleSerializer
    lookup_field = 'riddle_id'
    http_method_names = ['get', 'head', 'options']
    trap_count = 0

    def retrive(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @action(detail=True, methods=['get'], url_path='verify')
    def validate_answer(self, request, riddle_id=None):
        answer = request.query_params.get('answer')
        print(answer)
        riddle = self.get_object()
        print(riddle.answer)

        if answer is None:
            return Response({"detail":"Answer query parameter is required"}, status=400)
        if riddle.answer.lower() == answer.lower() and riddle.is_trap == False:
            return Response({"detail": "Correct Answer!"}, status=200)
        else:
            return Response({"detail": "This was a Trap. Try again!"}, status=400)

class RiddleByLevelAPIView(viewsets.ModelViewSet):
    serializer_class = RiddleSerializer
    http_method_names = ['get', 'options']

    def get_queryset(self):
        level = self.kwargs.get('level')
        return Riddles.objects.filter(level=level)
