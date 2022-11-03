from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from serializers import main as serializers
from . import models


class CreateView(generics.CreateAPIView):
    serializer_class = serializers.TestSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(who_created=self.request.user)

class ListView(generics.ListAPIView):
    serializer_class = serializers.TestSerializer
    
    def get_queryset(self):
        return models.Test.objects.all()
