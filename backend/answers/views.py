from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from serializers import main as serializers
from . import models


class CreateView(generics.CreateAPIView):
    serializer_class = serializers.AnswerSerializer
    permission_classes = [IsAuthenticated]

class ListView(generics.ListAPIView):
    serializer_class = serializers.AnswerSerializer
    
    def get_queryset(self):
        return models.Answer.objects.all()

