from rest_framework import serializers
from groups.models import Group
from activities.api.serializer import ActivitySerializer
from goals.api.serializer import GoalSerializer
from users.api.serializer import GetUserSerializer, UserSerializer


class GroupSerializer(serializers.ModelSerializer):
    creator = GetUserSerializer(many=False)
    users_on_group = GetUserSerializer(many=True)
    goals = GoalSerializer(many=True, read_only=True)
    activities = ActivitySerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = ['id', 'name', 'description',
                  'category', 'creator', 'users_on_group', 'goals', 'activities']


class GroupCreatorSerializer(serializers.ModelSerializer):
    creator = GetUserSerializer
    users_on_group = GetUserSerializer
    goals = GoalSerializer(many=True, read_only=True)
    activities = ActivitySerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = ['id', 'name', 'description',
                  'category', 'creator', 'users_on_group', 'goals', 'activities']
