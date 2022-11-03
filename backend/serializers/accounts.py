from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255, required=True)
    password = serializers.CharField(max_length=255, required=True)
    first_name = serializers.CharField(max_length=128, required=False, default='')
    last_name = serializers.CharField(max_length=128, required=False, default='')
    
    
    def save(self):
        return User.objects.create_user(**self.validated_data)
        
        
