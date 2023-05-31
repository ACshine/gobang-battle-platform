import json
import json
import operator

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from User.models import Player
from django.contrib.auth.models import User
from User.serializers import UserSerializer
from User.serializers import PlayerSerializer
from User.serializers import PostSerializer
from User.models import Post
class PostInfoView(APIView):
    def get(self,request):
        permission_classes = ([IsAuthenticated])  # 需要做验证
        id = json.loads(request.query_params.get('userid'))  # 注意这种取参数的方式！！！
        user = User.objects.get(id=id)
        player = Player.objects.get(user=user)
        posts=player.posts.all()
        serializer = PostSerializer(posts, many=True)
        return Response(
            {
                "posts":  serializer.data,
            }
        )
    def post(self,request):
        permission_classes = ([IsAuthenticated])  # 需要做验证
        content=request.data.get('content')
        user=request.user
        player = Player.objects.get(user=user)
        post=Post(content=content,player=player)
        post.save()
        return Response(
            {
                "result": "success"
            }
        )
    def delete(self,request):
        permission_classes = ([IsAuthenticated])  # 需要做验证
        post_id = request.data.get('post_id')
        user = request.user
        player = Player.objects.get(user=user)
        player.posts.filter(id=post_id).delete()

        return Response(
            {
                "result": "success"
            }
        )

