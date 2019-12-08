from rest_framework.exceptions import APIException


class EmailAuthComplete(APIException):
    status_code = 470
    default_detail = "This email is already authenticated."


class EmailNotRequestAuth(APIException):
    status_code = 471
    default_detail = "This email has not been requested for authentication"


class AuthCodeDoseNotMatch(APIException):
    status_code = 472
    default_detail = "The authentication number does not match."


class NotPermissionEmail(APIException):
    status_code = 473
    default_detail = "You don't have permission for that email."


class EmailExists(APIException):
    status_code = 474
    default_detail = "This email is already used for sign up."
