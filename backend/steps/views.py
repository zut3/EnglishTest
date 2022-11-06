from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from serializers import main as serializers
from . import models


class CreateView(generics.CreateAPIView):
    serializer_class = serializers.StepSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        test = serializer.validated_data['test'] 
        if test.who_create != self.request.user:
            raise ValidationError('cant change test, that dont belong you')
        
        serializer.save()
        

class ListView(generics.ListAPIView):
    serializer_class = serializers.StepSerializer
    
    def get_queryset(self):
        return models.Step.objects.all()

