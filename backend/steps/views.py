from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from serializers import main as serializers
from . import models


class CreateView(generics.CreateAPIView):
    serializer_class = serializers.StepSerializer
    permission_classes = [IsAuthenticated]


class ListView(generics.ListAPIView):
    serializer_class = serializers.StepSerializer
    
    def get_queryset(self):
        return models.Step.objects.all()

