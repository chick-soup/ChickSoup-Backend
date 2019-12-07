from django.urls import path

from .views import MyProfileAPI

urlpatterns = [
    path('my', MyProfileAPI.as_view()),
]