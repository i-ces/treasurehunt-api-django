from django.urls import path, include
from rest_framework import routers

from .views import RiddleViewSet, RiddleByLevelAPIView
from .views import RiddleListCreateAPIView
from .views import RiddleListCreateAPIView, LoginApiView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register(r"riddles", RiddleListCreateAPIView, basename="riddles")
router.register(r"", LoginApiView, basename="login")

# router.register(r')
urlpatterns = [
    path("api/", include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
