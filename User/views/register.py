from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from User.models import Player


class PlayerView(APIView):
    def post(self, request):
        data = request.POST
        username = data.get("username", "").strip()
        password = data.get("password", "").strip()
        confirmedPassword = data.get("confirmedPassword", "").strip()
        if not username or not password:
            return Response({
                'result': "用户名和密码不能为空"
            })
        if password != confirmedPassword:
            return Response({
                'result': "两个密码不一致",
            })
        if User.objects.filter(username=username).exists():
            return Response({
                'result': "用户名已存在"
            })
        user = User(username=username)
        user.set_password(password)
        user.save()
        Player.objects.create(user=user)
        return Response({
            'result': "success",
        })
