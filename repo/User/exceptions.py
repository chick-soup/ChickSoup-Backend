from rest_framework.exceptions import APIException


class UnauthenticatedEmail(APIException):
    status_code = 471
    default_detail = "This email is not validated."


class UserNotFound(APIException):
    status_code = 404
    default_detail = "user who has this primary key is not exist."


class IdNotExist(APIException):
    status_code = 470
    default_detail = "That email does not exist."


class IdAndPwNotMatch(APIException):
    status_code = 471
    default_detail = "ID and password do not match."


class ExpiredJWT(APIException):
    status_code = 403
    default_detail = "This JWT is expired."


class NoIncludeJWT(APIException):
    status_code = 401
    default_detail = "You should include JWT in headers with Authorization."


class IncorrectJWT(APIException):
    status_code = 422
    default_detail = "You included JWT which is incorrect."

