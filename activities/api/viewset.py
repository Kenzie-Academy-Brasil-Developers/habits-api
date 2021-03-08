from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from .serializer import ActivitySerializer
from activities.models import Activity


class ActivityViewSet(ModelViewSet):
        queryset = Activity.objects.all()
        serializer_class = ActivitySerializer
        permission_classes = [IsAuthenticatedOrReadOnly]