from django.urls import path

from .views import (
    MyProfileAPI,
    PkProfileAPI
)
urlpatterns = [
    path('my/profile', MyProfileAPI.as_view()),
    path("<int:user_id>/profile", PkProfileAPI.as_view()),
]