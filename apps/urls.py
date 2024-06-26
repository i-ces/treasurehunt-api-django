from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import (
    LoginApiView,
    RiddleByLevelAPIView,
    RiddleViewSet,
    UserProgressViewSet,
)

router = routers.DefaultRouter()
router.register(r"riddles", RiddleViewSet, basename="riddles")
router.register(r"level/(?P<level>\d+)", RiddleByLevelAPIView, basename="level")
router.register(r"user-progress", UserProgressViewSet, basename="usr-progress")

router.register(r"", LoginApiView, basename="login")

# router.register(r')
urlpatterns = [
    path("api/", include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
