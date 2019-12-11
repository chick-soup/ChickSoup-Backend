from rest_framework import serializers


class MyProfilePutSerializer(serializers.Serializer):
    nickname = serializers.CharField(max_length=12)
    status_message = serializers.CharField(max_length=100)
    where = serializers.CharField(max_length=10)
