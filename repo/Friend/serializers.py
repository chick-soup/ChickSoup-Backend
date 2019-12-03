from rest_framework import serializers


class RegisterFriendSerializers(serializers.Serializer):
    guest_id = serializers.IntegerField()

    bookmark = serializers.BooleanField()

    hidden = serializers.BooleanField()

    mute = serializers.BooleanField()