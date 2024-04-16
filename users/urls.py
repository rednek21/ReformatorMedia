from django.urls import path

from api.views import UserListAPIView

app_name = 'users'

urlpatterns = [
    path('users/', UserListAPIView.as_view(), name='users'),
]
