from django.urls import path

from .views import (
    SignUpAPI
)

urlpatterns = [
    path('signup/', SignUpAPI.as_view()),
]
