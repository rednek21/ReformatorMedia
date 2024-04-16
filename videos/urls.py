from django.urls import path

from videos.views import VideoListAPIView, VideoCreateAPIView

app_name = 'videos'

urlpatterns = [
    path('videos/', VideoListAPIView.as_view(), name='videos'),
    path('videos/create', VideoCreateAPIView.as_view(), name='videos_create'),
]
