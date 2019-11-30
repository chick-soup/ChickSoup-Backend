from django.urls import path

from .views import (
    EmailCheckAPI
)

urlpatterns = [
    path('check/', EmailCheckAPI.as_view())
]
