from rest_framework.serializers import ModelSerializer
from habits.models import Habit


class HabitSerializer(ModelSerializer):

    class Meta:
        model = Habit
        fields = ['id', 'title', 'category', 'difficulty', 'frequency', 'achieved', 'user']
