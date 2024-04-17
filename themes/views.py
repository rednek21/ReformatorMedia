from rest_framework import permissions
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend

from .models import Theme
from .serializers import ThemeSerializer


class ThemeListAPIView(ListAPIView):
    queryset = Theme.objects.all()
    model = Theme
    serializer_class = ThemeSerializer

    filterset_fields = ['id', 'title']
    # search_fields = ['username', 'email']

    filter_backends = [
        DjangoFilterBackend
    ]

    permission_classes = [
        permissions.AllowAny
    ]


class ThemeCreateAPIView(CreateAPIView):
    serializer_class = ThemeSerializer
    permission_classes = [
        permissions.AllowAny # После реализации работы с пользователем заменить на самописный permission для редакторов
    ]


class ThemeRetrieveAPIView(RetrieveAPIView):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer

    permission_classes = [
        permissions.AllowAny
    ]


class ThemeRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer

    permission_classes = [
        permissions.AllowAny
    ]


class ThemeDestroyAPIView(DestroyAPIView):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer

    permission_classes = [
        permissions.AllowAny
    ]
