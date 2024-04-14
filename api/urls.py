from django.urls import path

from api.views import UserListAPIView

app_name = 'api'

urlpatterns = [
    path('users-all/', UserListAPIView.as_view(), name='users_all'),
]
