from rest_framework import permissions
from rest_framework.generics import ListAPIView, CreateAPIView

from django_filters.rest_framework import DjangoFilterBackend

from .models import Video
from .serializers import VideoSerializer


class VideoListAPIView(ListAPIView):
    queryset = Video.objects.all()
    model = Video
    serializer_class = VideoSerializer

    filterset_fields = ['id', 'title', 'theme']
    # search_fields = ['username', 'email']

    filter_backends = [
        DjangoFilterBackend
    ]

    permission_classes = [
        permissions.AllowAny
    ]


class VideoCreateAPIView(CreateAPIView):
    serializer_class = VideoSerializer
    permission_classes = [
        permissions.AllowAny # После реализации работы с пользователем заменить на самописный permission для редакторов
    ]


