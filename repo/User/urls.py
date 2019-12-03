from django.urls import path

from .views import (
    SignUpAPI,
    RegisterFriendApi,
    FindFriendApi
)

urlpatterns = [
    path('signup', SignUpAPI.as_view()),
    path('friend', RegisterFriendApi.as_view()),
    path('friends', FindFriendApi.as_view())
]
