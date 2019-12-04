from django.urls import path

from .views import (
    SignUpAPI,
    SignUpProfileAPI
)

urlpatterns = [
    path('signup', SignUpAPI.as_view()),
    path('signup/profile', SignUpProfileAPI.as_view()),
]
