from rest_framework import serializers


class RegisterFriendSerializers(serializers.Serializer):
    guest_id = serializers.IntegerField()