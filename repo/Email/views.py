from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class EmailCheckAPI(APIView):
    def get(self, request):
        return Response("hello world!", status=status.HTTP_200_OK)
