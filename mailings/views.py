from django.shortcuts import render

from djoser import email
from rest_framework.generics import CreateAPIView

from mailings.models import UserActivationMailing
from mailings.serializers import UserActivationMailingSerializer


class UserActivationEmail(email.ActivationEmail):
    template_name = 'mailings/user_activation.html'

    def send(self, to, *args, **kwargs):
        super().send(to, *args, **kwargs)
        UserActivationMailing.objects.create(user=to)


# class UserActivationMailingCreateAPIView(CreateAPIView):
#     queryset = UserActivationMailing.objects.all()
#     serializer_class = UserActivationMailingSerializer
#     permission_classes = [
#
#     ]
