from django.urls import path
from .views import KakaoProfileAPI

urlpatterns = [
    path("<str:kakao_id>", KakaoProfileAPI.as_view()),
]