from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from .serializers import RiddleSerializer
from .models import Riddles


class RiddleListCreateAPIView(viewsets.ViewSet):
    @action(detail=False, methods=['get', 'post'], url_path=r'(?P<level>\d+)')
    def by_level(self, request, level=None):
        riddles = Riddles.objects.filter(level=level)
        serializer_class = RiddleSerializer(riddles, many=True)
        return Response(serializer_class.data)
