from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Video
from .serializers import VideoSerializer

from themes.models import Theme


class VideoTest(APITestCase):
    def setUp(self):
        self.theme1 = Theme.objects.create(title='Политика')
        self.theme2 = Theme.objects.create(title='О насущном')
        self.video1 = Video.objects.create(title='Video 1', theme_id=self.theme1.id, url='https://0.0.0.0/')
        self.video2 = Video.objects.create(title='Video 2', theme_id=self.theme2.id, url='https://0.0.0.0/https://0.0.0.0/')
        self. videoCount = Video.objects.count()

    def test_create_video(self):
        url = reverse('videos:videos_create')
        data = {
            'title': 'Тестовые приколы',
            'theme_id': self.theme2.id,
            'url': 'https://0.0.0.0/https://0.0.0.0/https://0.0.0.0/',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Video.objects.count(), self.videoCount + 1)
        self.assertEqual(Video.objects.last().title, 'Тестовые приколы')

    def test_list_videos(self):
        url = reverse('videos:videos_list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        videos = Video.objects.all()
        serializer = VideoSerializer(videos, many=True)
        self.assertEqual(response.data, serializer.data)

    def test_retrieve_videos(self):
        video1 = self.video1
        serializer = VideoSerializer(video1)

        url = reverse('videos:videos_retrieve', args={video1.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_update_videos(self):
        video1 = self.video1

        url = reverse('videos:videos_update', args={video1.id})

        data = {
            'title': 'Updated Video 1',
            'theme_id': video1.theme.id,
            'url': video1.url
        }
        response = self.client.put(url, data, format='json')
        video1.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Video.objects.count(), self.videoCount)
        self.assertEqual(video1.title, 'Updated Video 1')

    def test_destroy_videos(self):
        video2 = self.video2

        url = reverse('videos:videos_destroy', args={video2.id})

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Video.objects.count(), self.videoCount - 1)
        self.assertFalse(Video.objects.filter(id=video2.id).exists())
