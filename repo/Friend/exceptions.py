from rest_framework.exceptions import APIException


class CustomException(APIException):
    status_code = 111
    default_detail = "Create your exception message"
