from rest_framework.serializers import ModelSerializer
from activities.models import Activity


class ActivitySerializer(ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'title', 'realization_time', 'group']
