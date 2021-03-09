from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from .serializer import ActivitySerializer
from activities.models import Activity


class ActivityViewSet(ModelViewSet):
        serializer_class = ActivitySerializer
        permission_classes = [IsAuthenticatedOrReadOnly]

        def get_queryset(self):
                group = self.request.query_params.get('group')

                queryset = Activity.objects.all()

                if group:
                   queryset = queryset.filter(group_id=group)

                return queryset