from django.urls import path

from .views import ThemeListAPIView, ThemeCreateAPIView

app_name = 'themes'

urlpatterns = [
    path('themes/', ThemeListAPIView.as_view(), name='themes'),
    path('themes/create', ThemeCreateAPIView.as_view(), name='themes_create'),
]
