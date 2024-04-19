from rest_framework import permissions
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView

from django_filters.rest_framework import DjangoFilterBackend

from .models import Video
from .serializers import VideoSerializer


class VideoListAPIView(ListAPIView):
    queryset = Video.objects.all()
    model = Video
    serializer_class = VideoSerializer

    filterset_fields = ['theme']
    search_fields = ['title', 'url']

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter
    ]

    permission_classes = [
        permissions.AllowAny
    ]


class VideoCreateAPIView(CreateAPIView):
    serializer_class = VideoSerializer
    permission_classes = [
        permissions.AllowAny # После реализации работы с пользователем заменить на самописный permission для редакторов
    ]


class ThemeRetrieveAPIView(RetrieveAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    permission_classes = [
        permissions.AllowAny
    ]


class ThemeRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    permission_classes = [
        permissions.AllowAny
    ]


class ThemeDestroyAPIView(DestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    permission_classes = [
        permissions.AllowAny
    ]
