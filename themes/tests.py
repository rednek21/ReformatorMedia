from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Theme
from .serializers import ThemeSerializer


class ThemeTest(APITestCase):
    def setUp(self):
        self.theme = Theme.objects.create(title='Theme 1')
        self.ThemeCount = Theme.objects.count()

    def test_create_theme(self):
        url = reverse('themes:themes_create')
        data = {'title': 'Тестовые приколы'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Theme.objects.count(), self.ThemeCount + 1)
        self.assertEqual(Theme.objects.last().title, 'Тестовые приколы')

    def test_list_themes(self):
        url = reverse('themes:themes_list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        themes = Theme.objects.all()
        serializer = ThemeSerializer(themes, many=True)
        self.assertEqual(response.data, serializer.data)

    def test_retrieve_themes(self):
        theme = self.theme
        serializer = ThemeSerializer(theme)
        url = reverse('themes:themes_retrieve', args={theme.id})

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_update_themes(self):
        theme = self.theme

        url = reverse('themes:themes_update', args={theme.id})

        data = {'title': 'Updated Theme 1'}
        response = self.client.put(url, data, format='json')
        theme.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Theme.objects.count(), self.ThemeCount)
        self.assertEqual(theme.title, 'Updated Theme 1')

    def test_destroy_themes(self):
        theme = self.theme

        url = reverse('themes:themes_destroy', args={theme.id})

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Theme.objects.count(), self.ThemeCount - 1)
        self.assertFalse(Theme.objects.filter(id=theme.id).exists())
