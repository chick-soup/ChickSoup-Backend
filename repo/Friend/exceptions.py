from rest_framework.exceptions import APIException


class FriendNotFound(APIException):
    status_code = 470
    default_detail = "The user for this friend_id is not exist"


class AlreadyFriend(APIException):
    status_code = 471
    default_detail = "This is the user who has already sent the friend request."
