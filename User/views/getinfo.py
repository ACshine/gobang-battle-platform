import json

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from User.models import Player
from django.contrib.auth.models import User
from User.serializers import UserSerializer
from User.serializers import PlayerSerializer
class InfoView(APIView):

    # def get(self, request,format=None):
    #     user = request.user#当前用户
    #     player = Player.objects.get(user=user)

    def get(self, request):
        permission_classes = ([IsAuthenticated])  # 需要做验证
        id = json.loads(request.query_params.get('userid')) # 注意这种取参数的方式！！！
        user = User.objects.get(id=id)
        player = Player.objects.get(user=user)
        myuser=request.user
        myplayer=Player.objects.get(user=myuser)
        is_follow=False
        fans = player.followers.all()

        if myplayer.user.id != player.user.id:
            if myplayer in fans:
                is_follow=True
            else:
                is_follow=False
        return Response({
        'id':user.id,
        'result': "success",
        'username': user.username,
        'photo': player.photo,
        'coins': player.coins,
        'fanscount': player.fanscount,
        'is_sign_in': player.is_sign_in,
        'sign_in_coins': player.sign_in_coins,
        'is_follow':is_follow,
       })



    def put(self, request):
        permission_classes = ([IsAuthenticated])  # 需要做验证
        user = request.user  # 当前用户
        player = Player.objects.get(user=user)
        Player.objects.filter(user=user).update(is_sign_in=False)
        return Response({
            'is_sign_in': False,
        })


