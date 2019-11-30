from rest_framework.exceptions import APIException


class EmailExists(APIException):
    status_code = 470
    default_detail = "This email is already used."
