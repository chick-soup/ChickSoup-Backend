from django.urls import path

from .views import (
    RegisterFriendApi,
    FindFriendApi
)

urlpatterns = [
    path('friend', RegisterFriendApi.as_view()),
    path('friends', FindFriendApi.as_view())
]
