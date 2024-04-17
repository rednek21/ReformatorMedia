from django.urls import path

from .views import ThemeListAPIView, ThemeCreateAPIView, ThemeRetrieveUpdateAPIView, ThemeDestroyAPIView, ThemeRetrieveAPIView

app_name = 'themes'

urlpatterns = [
    path('themes/', ThemeListAPIView.as_view(), name='themes_list'),
    path('themes/create', ThemeCreateAPIView.as_view(), name='themes_create'),
    path('themes/<int:pk>', ThemeRetrieveAPIView.as_view(), name='themes_retrieve'),
    path('themes/<int:pk>/update', ThemeRetrieveUpdateAPIView.as_view(), name='themes_update'),
    path('themes/<int:pk>/destroy', ThemeDestroyAPIView.as_view(), name='themes'),
]