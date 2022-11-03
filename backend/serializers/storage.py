from rest_framework import serializers
from storage.models import Image

class ImageSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Image
        fields = '__all__'

