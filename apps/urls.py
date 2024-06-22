from django.urls import path, include
from rest_framework import routers

from .views import RiddleListCreateAPIView

router = routers.DefaultRouter()
router.register(r"riddles", RiddleListCreateAPIView, basename="riddles")
# router.register(r')
urlpatterns = [
    path("api/", include(router.urls))
]
