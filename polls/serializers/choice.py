
from rest_framework import serializers
from polls.models import Choice

class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Choice
        fields = ['question', 'choice_text', 'votes']