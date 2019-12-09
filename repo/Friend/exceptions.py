from rest_framework.exceptions import APIException


class FriendNotFound(APIException):
    status_code = 470
    default_detail = "The user for this friend_id is not exist"


class AlreadyRequest(APIException):
    status_code = 471
    default_detail = "This is the user who has already sent the friend request."


class AlreadyFriend(APIException):
    status_code = 472
    default_detail = "This is the user who is already a friend."


class Myself(APIException):
    status_code = 473
    default_detail = "You cannot send a request to add a friend to yourself."


class NotFriend(APIException):
    status_code = 471
    default_detail = "You are not friends with that user."
