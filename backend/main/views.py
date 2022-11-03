from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from serializers import main as serializers
from . import models

class TestsView(generics.ListAPIView):
    serializer_class = serializers.TestSerializer
    
    def get_queryset(self):
        return models.Test.objects.all()

class CreateTests(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.TestSerializer
    
    def get_queryset(self):
        return models.Test.objects.all()

