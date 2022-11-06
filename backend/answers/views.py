from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from serializers import main as serializers
from . import models


class CreateView(generics.CreateAPIView):
    serializer_class = serializers.AnswerSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        step = serializer.validated_data['step']

        if step.test.who_create != self.request.user:
            raise ValidationError('cant change test, that dont belong you')
        
        serializer.save()


class ListView(generics.ListAPIView):
    serializer_class = serializers.AnswerSerializer
    lookup_field = 'answers'
    
    def get_queryset(self):
        return models.Answer.objects.all()

