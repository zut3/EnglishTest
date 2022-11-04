from rest_framework import serializers
from tests.models import Test
from steps.models import Step
from answers.models import Answer

class AnswerSerializer(serializers.ModelSerializer):
    id = serializers.CharField(max_length=36, read_only=True)
    is_true = serializers.BooleanField(write_only=True)

    class Meta:
        fields = '__all__'
        model = Answer


class StepSerializer(serializers.ModelSerializer):
    id = serializers.CharField(max_length=36, read_only=True)
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        fields = '__all__' 
        model = Step


class TestSerializer(serializers.ModelSerializer):
    id = serializers.CharField(max_length=36, read_only=True)
    steps = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    who_create = serializers.PrimaryKeyRelatedField(read_only=True)
    steps = StepSerializer(many=True, read_only=True)

    class Meta:
        fields = '__all__'
        model = Test

   
