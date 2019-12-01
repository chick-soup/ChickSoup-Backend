from django.urls import path

from .views import (
    EmailCheckAPI,
    EmailAuthAPI
)

urlpatterns = [
    path('check/', EmailCheckAPI.as_view()),
    path('auth/', EmailAuthAPI.as_view())
]
