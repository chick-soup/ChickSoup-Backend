from django.urls import path

from .views import (
    MyProfileAPI,
    PkProfileAPI
)
urlpatterns = [
    path('my', MyProfileAPI.as_view()),
    path("<int:user_id>", PkProfileAPI.as_view()),
]