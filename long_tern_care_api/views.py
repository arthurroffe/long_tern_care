from django.shortcuts import render

# Create your views here.
from long_tern_care_api.models import User
from long_tern_care_api.serializers import UserSerializer

from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer