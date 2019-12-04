from django.urls import path

from .views import (
    SignUpAPI,
    SignUpProfileAPI,
    LoginAPI
)

urlpatterns = [
    path('signup', SignUpAPI.as_view()),
    path('signup/profile', SignUpProfileAPI.as_view()),
    path('login', LoginAPI.as_view()),
]
