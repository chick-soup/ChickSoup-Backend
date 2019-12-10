from rest_framework.exceptions import APIException


class NotFriend(APIException):
    status_code = 470
    default_detail = "You are not friends with that user."
