from rest_framework import serializers
from .models import EmailAuth


class EmailCheckSerializers(serializers.Serializer):
    email = serializers.CharField(max_length=30)


class EmailAuthSerializers(serializers.Serializer):
    email = serializers.CharField(max_length=30)
    auth_code = serializers.CharField()
