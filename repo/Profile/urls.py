from django.urls import path

from .views import (
    MyProfileAPI,
    UserIdAPI,
)
from Kakao.views import MyKakaoIdAPI
from Friend.views import (
    FriendListAPI,
    MuteListAPI,
    HiddenListAPI,
    UserIdFriendAPI,
    FriendRequestListAPI,
    FriendResponseListAPI
)

urlpatterns = [
    path('my/profile', MyProfileAPI.as_view()),
    path('my/kakao-id', MyKakaoIdAPI.as_view()),
    path('my/friends', FriendListAPI.as_view()),
    path('my/friends/mute', MuteListAPI.as_view()),
    path('my/friends/hidden', HiddenListAPI.as_view()),
    path('my/friends/request', FriendRequestListAPI.as_view()),
    path('my/friends/response', FriendResponseListAPI.as_view()),
    path('my/friends/<int:guest_id>', UserIdFriendAPI.as_view()),
    path("<int:user_id>", UserIdAPI.as_view()),
]
