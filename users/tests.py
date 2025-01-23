from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User


class UserTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            email='user@test.com',
            first_name='Test',
            last_name='User'
        )
        self.user.set_password('test123')
        self.user.save()

        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

    def test_create_user(self):

        url = reverse('users:users-list')
        data = {
            'email': 'newuser@testing.com',
            'password': 'newpassword123',
            'first_name': 'Test',
            'last_name': 'Testov'
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(email='newuser@testing.com').exists())

    def test_retrieve_user(self):

        url = reverse('users:users-detail', kwargs={'pk': self.user.id})

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_list_users(self):

        url = reverse('users:users-list')

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_user(self):

        url = reverse('users:users-detail', kwargs={'pk': self.user.id})
        update_data = {
            'first_name': 'Andrey',
            'last_name': 'Andreev'
        }

        response = self.client.patch(url, update_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, 'Andrey')
        self.assertEqual(self.user.last_name, 'Andreev')

    def test_delete_user(self):

        url = reverse('users:users-detail', kwargs={'pk': self.user.id})

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(User.objects.filter(id=self.user.id).exists())