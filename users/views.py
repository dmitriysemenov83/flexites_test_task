from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from users.models import User
# from users.paginators import PageNumberPaginator
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    # pagination_class = PageNumberPaginator

    def get_permissions(self):
        if self.action in ['create']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
