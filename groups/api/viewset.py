from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from groups.models import Group
from .serializer import GroupSerializer
from rest_framework.filters import SearchFilter
from rest_framework.decorators import action
from rest_framework.response import Response
from users.api.serializer import UserSerializer


class GroupViewSet(ModelViewSet):
    serializer_class = GroupSerializer
    filter_backends = [SearchFilter]
    permission_classes = [IsAuthenticatedOrReadOnly]
    search_fields = ['name']

    def get_queryset(self):
        category = self.request.query_params.get('category')

        queryset = Group.objects.all()

        if category:
            queryset = queryset.filter(category__icontains=category)

        return queryset

    # POST /groups/1/subscribe
    @action(methods=['POST'], detail=True)
    def subscribe(self, request, pk=None):
        request.user.group_id = pk
        request.user.save()

        user = UserSerializer(request.user)

        return Response({'message': 'User inserted on group', 'user': user.data})
