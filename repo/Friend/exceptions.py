from rest_framework.exceptions import APIException


class FriendNotFound(APIException):
    status_code = 470
    default_detail = "The user for this friend_id is not exist"
