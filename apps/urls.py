from django.urls import path, include
from rest_framework import routers

from .views import RiddleViewSet, RiddleByLevelAPIView, LoginApiView, UserProgressViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register(r"riddles", RiddleViewSet, basename="riddles")
router.register(r"level/(?P<level>\d+)", RiddleByLevelAPIView, basename="level")
router.register(r'user-progress', UserProgressViewSet, basename="usr-progress")

router.register(r"", LoginApiView, basename="login")

# router.register(r')
urlpatterns = [
    path("api/", include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
