from rest_framework.views import APIView
from rest_framework.response import Response
from User.models import Player
import numpy as np
from rest_framework.permissions import IsAuthenticated
from decimal import *
class SignInfoView(APIView):
    def put(self,request):
        permission_classes = ([IsAuthenticated])  # 需要做验证
        user = request.user  # 当前用户
        fg=np.random.choice([0,1], p=[0.99,0.01])
        if(fg==0):
            res=np.random.uniform(0.01,10)
        else:
            res=100.00
        res=Decimal.from_float(res)
        res=Decimal(res).quantize(Decimal('0.00'))
        player = Player.objects.get(user=user)
        Player.objects.filter(user=user).update(is_sign_in=True, coins=player.coins + res,sign_in_coins=res)


        return Response({
            'result': "success",
            'username': user.username,
            'photo': player.photo,
            'coins': player.coins+res,
            'fanscount': player.fanscount,
            'is_sign_in': True,
            'sign_in_coins': res,
        })

