from django.urls import path
from User.views.getinfo import InfoView
from User.views.register import PlayerView
from User.views.getuserlist import ListInfoView
from User.views.signinInfo import SignInfoView
from User.views.follow import FollowView
from User.views.PostInfo import PostInfoView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', PlayerView.as_view()),
    path('getinfo/', InfoView.as_view()),
    path('userlist/', ListInfoView.as_view()),
    path('signininfo/',SignInfoView.as_view()),
    path('follow/', FollowView.as_view()),
    path('post/', PostInfoView.as_view()),
]
