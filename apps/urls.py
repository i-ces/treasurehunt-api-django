from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

from .views import (
    LoginApiView,
    RiddleByLevelAPIView,
    RiddleViewSet,
    UserProgressViewSet,
    LevelViewSet
)

router = routers.DefaultRouter()
router.register(r"levels", LevelViewSet, basename="levels")
router.register(r"level/(?P<level>\d+)", RiddleByLevelAPIView, basename="level")
router.register(r"level/(?P<level>\d+)/riddles", RiddleViewSet, basename="riddles")
router.register(r"user-progress", UserProgressViewSet, basename="usr-progress")

router.register(r"", LoginApiView, basename="login")

urlpatterns = [
    path("api/", include(router.urls)),
    path("token/", views.obtain_auth_token, name='api-token'),
]
