from rest_framework.exceptions import APIException


class EmailExists(APIException):
    status_code = 470
    default_detail = "This email is already used."


class EmailNotRequestAuth(APIException):
    status_code = 471
    default_detail = "This email has not been requested for authentication"
