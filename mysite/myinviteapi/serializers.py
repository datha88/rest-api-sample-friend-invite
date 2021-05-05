# serializers.py
from rest_framework import serializers

from .models import Friend

class FriendSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Friend
        fields = ('name', 'email')
