from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from .serializer import GoalSerializer
from goals.models import Goal


class GoalViewSet(ModelViewSet):
        queryset = Goal.objects.all()
        serializer_class = GoalSerializer
        permission_classes = [IsAuthenticatedOrReadOnly]