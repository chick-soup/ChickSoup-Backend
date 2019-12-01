from rest_framework.exceptions import APIException


class UnauthenticatedEmail(APIException):
    status_code = 471
    default_detail = "This email is not validated."
