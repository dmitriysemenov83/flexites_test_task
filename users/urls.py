from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users.apps import UsersConfig
from users.views import UserViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = UsersConfig.name

usr_router = DefaultRouter()
usr_router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(usr_router.urls)),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]