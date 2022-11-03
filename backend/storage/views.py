from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from . import models
from serializers.storage import ImageSerializer


class LoadImage(generics.CreateAPIView):
    serializer_class = ImageSerializer

    def finalize_response(self, request, response, *args, **kwargs):
        if response.status_code == 201:
            response.data = {"success": 1, "file": {
                "url": response.data["image"]
            }}

        return super().finalize_response(request, response, *args, **kwargs) 



