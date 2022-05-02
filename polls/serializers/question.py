from rest_framework import serializers
from polls.models.choice import Choice
from polls.models.question import Question

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ['question_text', 'pub_date']

