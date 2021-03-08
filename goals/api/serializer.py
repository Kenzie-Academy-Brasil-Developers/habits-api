from rest_framework.serializers import ModelSerializer
from goals.models import Goal


class GoalSerializer(ModelSerializer):
    class Meta:
        model = Goal
        fields = ['id', 'title', 'difficulty', 'achieved', 'how_much_achieved', 'group']
