from rest_framework import serializers
from .models import Question

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

    # def create(self, validated_data):
    #     return Question.objects.create(**validated_data)
