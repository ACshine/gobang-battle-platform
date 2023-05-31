import json

from rest_framework.views import APIView
from rest_framework.response import Response
from User.models import Player
from User.serializers import PlayerSerializer
from rest_framework.permissions import IsAuthenticated
class ListInfoView(APIView):
    # def get(self,request):
    #     id = json.loads(request.query_params.get('userid')) # 注意这种取参数的方式！！！
    #     players=Player.objects.all().filter(id!=id)
    #     serializer = PlayerSerializer(players, many=True)
    #     return Response(serializer.data)
    def get(self, request):
        permission_classes = ([IsAuthenticated])  # 需要做验证
        id = json.loads(request.query_params.get('userid'))  # 注意这种取参数的方式！！！
        players = Player.objects.all()
        resp = []
        for player in players:
            if(player.user.id!=id):
                resp.append({
                    'id': player.user.id,
                    'username': player.user.username,
                    'photo': player.photo,
                    'fanscount': player.fanscount,
                })
        return Response(resp)