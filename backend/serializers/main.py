from rest_framework import serializers
from tests.models import Test
from steps.models import Step
from answers.models import Answer


class TestSerializer(serializers.ModelSerializer):
    id = serializers.CharField(max_length=36, read_only=True)

    class Meta:
        fields = '__all__'
        model = Test

class StepSerializer(serializers.ModelSerializer):
    id = serializers.CharField(max_length=36, read_only=True)

    class Meta:
        fields = '__all__'
        model = Step

class AnswerSerializer(serializers.ModelSerializer):
    id = serializers.CharField(max_length=36, read_only=True)

    class Meta:
        fields = '__all__'
        model = Answer
