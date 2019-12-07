from rest_framework import serializers


class SignUpSerializers(serializers.Serializer):
    email = serializers.CharField(max_length=30)
    password = serializers.CharField()


class ProfileSerializers(serializers.Serializer):
    nickname = serializers.CharField(max_length=12)
    profile = serializers.ImageField()


class LoginSerializers(serializers.Serializer):
    email = serializers.CharField(max_length=30)
    password = serializers.CharField()
