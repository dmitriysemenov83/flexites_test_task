from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User
from .models import Organization
from .serializers import OrganizationSerializer


class OrganizationAPITestCase(APITestCase):
    def setUp(self):
        # Создаем тестового пользователя
        self.user = User.objects.create(
            email='user@test.com',
            is_active=True
        )
        self.user.set_password('test123')
        self.user.save()

        # Генерация токена для аутентификации
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')


    def test_create_organization(self):

        url = reverse('organizations:organizations_create')
        data = {
            'name': 'Test Organization',
            'description': 'This is a test organization.'
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Organization.objects.filter(name='Test Organization').exists())


    def test_list_organizations(self):

        Organization.objects.create(name='Org 1', description='First organization.')

        url = reverse('organizations:organizations_list')

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
