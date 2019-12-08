from django.urls import path

from .views import (
    MyProfileAPI,
    PkProfileAPI
)
from Kakao.views import MyKakaoIdAPI

urlpatterns = [
    path('my/profile', MyProfileAPI.as_view()),
    path('my/kakao-id', MyKakaoIdAPI.as_view()),
    path("<int:user_id>", PkProfileAPI.as_view()),
]
