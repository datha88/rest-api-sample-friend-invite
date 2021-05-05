from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import FriendSerializer
from .models import Friend


class FriendViewSet(viewsets.ModelViewSet):
    queryset = Friend.objects.all().order_by('name')
    serializer_class = FriendSerializer
