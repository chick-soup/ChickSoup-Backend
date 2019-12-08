from rest_framework.exceptions import APIException


class InvalidKakaoId(APIException):
    status_code = 470
    default_detail = "There is no member matching the Kakao ID."
