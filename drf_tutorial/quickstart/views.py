from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import viewsets
from rest_framework import permissions

from .serializers import UserSerializer, GroupSerializer

User = get_user_model()


class UserQViewSet(viewsets.ModelViewSet):
    """
    API end point that allows users to be viewed or edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    lookup_field = "username"
    permission_classes = [permissions.IsAuthenticated, ]


class GroupQViewSet(viewsets.ModelViewSet):
    """
    API endpoint allows groups to be viewed or edited
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated, ]

