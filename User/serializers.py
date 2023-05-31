from rest_framework import serializers
from .models import Player
from .models import Post
from django.contrib.auth.models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=['id','username']

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        user = UserSerializer()
        fields=['user','coins','fanscount','photo']
        depth = 1

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields=['id','content']