from django.shortcuts import render
from rest_framework import viewsets
from pranjalmobile.models import signup
from pranjalmobile.serializers import signupSerializer


# Create your views here.


class signupviewset(viewsets.ModelViewSet):
    queryset = signup.objects.all()
    serializer_class = signupSerializer