from django.urls import path, include
from rest_framework import routers

from .views import RiddleViewSet, RiddleByLevelAPIView
from .views import RiddleListCreateAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register(r"riddle", RiddleViewSet, basename="level")
router.register(r"level/(?P<level>\d+)", RiddleByLevelAPIView,
                basename="riddles-by-level")

urlpatterns = [
    path("api/", include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
