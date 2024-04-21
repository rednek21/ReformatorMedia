# from django.urls import reverse
# from rest_framework import status
# from rest_framework.authtoken.models import Token
# from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate, APIClient
#
# from .models import User
# from .serializers import UserSerializer
# from .views import UserRetrieveAPIView
#
#
# class UserTest(APITestCase):
#     def setUp(self):
#         self.factory = APIRequestFactory()
#         self.user = User.objects.create(username='some_user', password='password123', email='some@mail.ru',
#                                         first_name='first name', last_name='last name')
#
#     def test_list_users(self):
#         url = reverse('users:users_list')
#
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#
#         response = self.client.get(url)
#
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data, serializer.data)
#
#     def test_registration_user(self):
#         url = reverse('user-list')
#
#         data = {
#             "email": "test@example.com",
#             "first_name": "first name",
#             "last_name": "last name",
#             "username": "test_user",
#             "password": "password123"
#         }
#
#         response = self.client.post(url, data, format='json')
#
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertTrue('username' in response.data)
#
#     def test_user_get_token(self):
#         url = '/auth/token/login/'
#         data = {'username': self.user.username, 'password': self.user.password}
#
#         response = self.client.post(url, data, format='json')
#
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertTrue('auth_token' in response.data)
#
#         # client = APIClient()
#         # token = Token.objects.get(user__username=self.user.username)
#         # client.force_authenticate(user=self.user, token=token)
#         #
#         # response = client.get()
#
#     def test_retrieve_users(self):
#         serializer = UserSerializer(self.user)
#
#         url = reverse('users:users_retrieve', args={self.user.id})
#         view = UserRetrieveAPIView.as_view()
#
#         # Try to authenticate
#         self.client.login(username=self.user.username, password=self.user.password)
#         # token = Token.objects.get(user__username=self.user.username)
#         token = Token.objects.create(user=self.user)
#         self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
#
#         request = self.client.get(url)
#         response = view(request)
#
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data, serializer.data)
#
#     def test_update_users(self):
#         theme = self.theme
#
#         url = reverse('themes:themes_update', args={theme.id})
#
#         data = {'title': 'Updated Theme 1'}
#         response = self.client.put(url, data, format='json')
#         theme.refresh_from_db()
#
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(Theme.objects.count(), self.ThemeCount)
#         self.assertEqual(theme.title, 'Updated Theme 1')
#
#     def test_destroy_themes(self):
#         theme = self.theme
#
#         url = reverse('themes:themes_destroy', args={theme.id})
#
#         response = self.client.delete(url)
#
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertEqual(Theme.objects.count(), self.ThemeCount - 1)
#         self.assertFalse(Theme.objects.filter(id=theme.id).exists())
