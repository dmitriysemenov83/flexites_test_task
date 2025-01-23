from django.urls import path, include
from organizations.apps import OrganizationsConfig
from organizations.views import OrganizationListAPIView, OrganizationCreateAPIView

app_name = OrganizationsConfig.name


urlpatterns = [
    path('', OrganizationListAPIView.as_view(), name='organizations_list'),
    path('create/', OrganizationCreateAPIView.as_view(), name='organizations_create'),
]