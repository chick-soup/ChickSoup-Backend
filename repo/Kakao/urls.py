from django.urls import path
from .views import KakaoProfileAPI

urlpatterns = [
    path("<str:kakao_id>/profile", KakaoProfileAPI.as_view()),
]