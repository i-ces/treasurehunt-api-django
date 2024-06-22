from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import RiddleSerializer
from .models import Riddles

class RiddleViewSet(viewsets.ModelViewSet):
    queryset = Riddles.objects.all()
    serializer_class = RiddleSerializer
    lookup_field = 'riddle_id'
    http_method_names = ['get', 'head', 'options']

    def retrive(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class RiddleByLevelAPIView(viewsets.ModelViewSet):
    serializer_class = RiddleSerializer

    def get_queryset(self):
        level = self.kwargs.get('level')
        return Riddles.objects.filter(level=level)