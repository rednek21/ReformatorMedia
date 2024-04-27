from django.http import HttpResponseNotFound
from django.shortcuts import render

from djoser import email

from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.views import APIView
from rest_framework import authentication, permissions

from mailings.models import UserActivationMailing
from mailings.serializers import UserActivationMailingSerializer

from django.utils import timezone

from users.models import User


class UserActivationEmail(email.ActivationEmail):
    template_name = 'mailings/user_activation.html'

    def send(self, to, *args, **kwargs):
        try:
            user = User.objects.get(email=str(to[0]))
            UserActivationMailing.objects.create(user=user, created_at=timezone.now(), verified=False)
            super().send(to, *args, **kwargs)
        except User.DoesNotExist:
            return HttpResponseNotFound("User not found")


# class UserActivationMailingVerifyAPIView(APIView):
#     # permission_classes = [
#     #     permissions.
#     # ]
#
#     authentication_classes = [authentication.TokenAuthentication]
#     permission_classes = [permissions.IsAdminUser]
