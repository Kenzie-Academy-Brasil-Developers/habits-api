from rest_framework import serializers
from groups.models import Group
from activities.api.serializer import ActivitySerializer
from goals.api.serializer import GoalSerializer
from users.api.serializer import UserSerializer


class GroupSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)
    goals = GoalSerializer(many=True, read_only=True)
    activities = ActivitySerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = ['id', 'name', 'description', 'category', 'users', 'goals', 'activities']
