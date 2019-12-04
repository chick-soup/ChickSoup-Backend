from django.urls import path

from .views import (
    RegisterFriendAPI
)

urlpatterns = [
    path('friend', RegisterFriendAPI.as_view()),
]
