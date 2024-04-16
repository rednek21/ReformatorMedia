from rest_framework import permissions
from rest_framework.generics import ListAPIView

from django_filters.rest_framework import DjangoFilterBackend

from user.models import User
from user.serializers import UserSerializer


class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    model = User
    serializer_class = UserSerializer

    filterset_fields = ['id', 'username', 'is_active']
    # search_fields = ['username', 'email']

    filter_backends = [
        DjangoFilterBackend
    ]

    permission_classes = [
        permissions.AllowAny
    ]


