from django.shortcuts import render

from djoser import email


# Create your views here.
class UserActivationEmail(email.ActivationEmail):
    template_name = 'mailings/user_activation.html'
