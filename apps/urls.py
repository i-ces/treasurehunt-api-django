from django.urls import path, include
from rest_framework import routers

from .views import RiddleViewSet, RiddleByLevelAPIView

router = routers.DefaultRouter()
router.register(r"riddle", RiddleViewSet, basename="level")
router.register(r"riddle_level/(?P<level>\d+)", RiddleByLevelAPIView, basename="riddles-by-level")

urlpatterns = [
    path("api/", include(router.urls)),
]
