from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from organizations.models import Organization
from organizations.serializers import OrganizationSerializer
# from users.paginators import PageNumberPaginator


class OrganizationCreateAPIView(generics.CreateAPIView):
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated]


class OrganizationListAPIView(generics.ListAPIView):
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()
    # pagination_class = PageNumberPaginator
    permission_classes = [IsAuthenticated]