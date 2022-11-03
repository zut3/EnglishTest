from rest_framework import serializers
from main import models

class TestSerializer(serializers.ModelSerializer):
    id = serializers.CharField(max_length=36, read_only=True)
    class Meta:
        fields = '__all__'
        model = models.Test

