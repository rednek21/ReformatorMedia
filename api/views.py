from rest_framework import permissions
from rest_framework.generics import ListAPIView

from user.models import User
from user.serializers import UserSerializer


class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    model = User
    serializer_class = UserSerializer
    permission_classes = [
        permissions.AllowAny
    ]
