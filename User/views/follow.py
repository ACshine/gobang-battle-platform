import json

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from User.models import Player
from django.contrib.auth.models import User
from User.serializers import UserSerializer
class FollowView(APIView):
    permission_classes = ([IsAuthenticated])#需要做验证
    def post(self, request):
        permission_classes = ([IsAuthenticated])  # 需要做验证
        user=request.user
        player = Player.objects.get(user=user)
        target_id = json.loads(request.data.get('target_id')) # 注意这种取参数的方式！！！
        target_user=User.objects.get(id=target_id)
        target_player = Player.objects.get(user=target_user)

        fans=target_player.followers.all()

        if player.user.id != target_player.user.id:
            if player in fans:
                target_player.followers.remove(player)
                Player.objects.filter(user=target_user).update(fanscount=target_player.fanscount-1)
            else:
                target_player.followers.add(player)
                Player.objects.filter(user=target_user).update(fanscount=target_player.fanscount + 1)
        return Response({
        'result': "success",
       })

