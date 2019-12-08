from django.urls import path
from .views import KakaIdAPI


urlpatterns = [
    path("<str:kakao_id>", KakaIdAPI.as_view()),
]
