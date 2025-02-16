from django.shortcuts import render
from django.contrib.auth.models import User
from user_api.models import MyGroup


from rest_framework import viewsets

from user_api.serializers import *


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer



class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = MyGroup.objects.all()
    serializer_class = GroupSerializer
