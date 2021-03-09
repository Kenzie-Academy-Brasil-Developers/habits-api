from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from .serializer import GoalSerializer
from goals.models import Goal


class GoalViewSet(ModelViewSet):
        serializer_class = GoalSerializer
        permission_classes = [IsAuthenticatedOrReadOnly]

        def get_queryset(self):
                group = self.request.query_params.get('group')

                queryset = Goal.objects.all()

                if group:
                   queryset = queryset.filter(group_id=group)

                return queryset