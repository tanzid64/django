from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from accounts.models import CustomUser as User
# Create your tests here.
class UserViewSetsTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(email='testuser@test.com', username='testuser', password='password123')

    def test_get_user_details(self):
        url = f'/api/accounts/{self.user.username}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.user.username)
        self.assertEqual(response.data['email'], self.user.email)
        self.assertEqual(response.data['first_name'], self.user.first_name)
        self.assertEqual(response.data['last_name'], self.user.last_name)
        self.assertEqual(response.data['is_staff'], self.user.is_staff)

    def test_register_user(self):
        url = '/api/accounts/'
        data = {
            "username": "newuser",
            "email": "tanzid3@gmail.com",
            "password": "blog1234",
            "password2": "blog1234"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['username'], 'newuser')

    def test_update_user_details(self):
        url = f'/api/accounts/{self.user.username}/'
        data = {
            'email': 'updated@example.com',
            'first_name': 'Updated',
            'last_name': 'User'
        }
        self.client.force_authenticate(user=self.user)
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], 'updated@example.com')
        self.assertEqual(response.data['first_name'], 'Updated')
        self.assertEqual(response.data['last_name'], 'User')

    def test_delete_user(self):
        url = f'/api/accounts/{self.user.username}/'
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_authorized_access(self):
        url = '/api/accounts/'
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_nonexistent_user_lookup(self):
        url = '/api/accounts/nonexistent/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class UserLoginViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='test@example.com', username='testuser', password='password123')

    def test_valid_login(self):
        data = {
            'email': 'test@example.com',
            'password': 'password123'
        }
        response = self.client.post('/api/login/', data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', response.data)
        self.assertIn('username', response.data)

    def test_invalid_login(self):
        data = {
            'email': 'test@example.com',
            'password': 'wrongpassword'
        }
        response = self.client.post('/api/login/', data, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.data)