from django.urls import path

from videos.views import VideoListAPIView, VideoCreateAPIView, ThemeRetrieveAPIView, ThemeRetrieveUpdateAPIView, ThemeDestroyAPIView

app_name = 'videos'

urlpatterns = [
    path('videos/', VideoListAPIView.as_view(), name='videos_list'),
    path('videos/create', VideoCreateAPIView.as_view(), name='videos_create'),
    path('videos/<int:pk>/', ThemeRetrieveAPIView.as_view(), name='videos_retrieve'),
    path('videos/<int:pk>/update', ThemeRetrieveUpdateAPIView.as_view(), name='videos_update'),
    path('videos/<int:pk>/destroy', ThemeDestroyAPIView.as_view(), name='videos_destroy'),
]
