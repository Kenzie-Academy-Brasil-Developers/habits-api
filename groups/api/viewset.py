from rest_framework.generics import get_object_or_404
from users.models import User
import ipdb
from rest_framework import serializers, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from groups.models import Group
from .serializer import GroupCreatorSerializer, GroupSerializer
from rest_framework.filters import SearchFilter
from rest_framework.decorators import action
from rest_framework.response import Response
from users.api.serializer import GetUserSerializer, UserSerializer


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

    def create(self, request, *args, **kwargs):

        user = User.objects.get(id=request.user.id)

        data = {
            **request.data,
            "creator": user.id,
            "users_on_group": [user.id]
        }

        serializer = GroupCreatorSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None, *args, **kwargs):
        group = Group.objects.get(pk=pk)

        if group.creator_id != request.user.id:
            return Response({'status': 'error', 'message': 'Only the group creator can update the group'}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = self.serializer_class(
            group, data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    # POST /groups/1/subscribe
    @action(methods=['POST'], detail=True)
    def subscribe(self, request, pk=None):

        user_group = Group.objects.filter(
            id=pk,
            users_on_group__id=request.user.id
        ).first()

        if user_group:
            return Response({'message': 'User already on group'}, status=status.HTTP_401_UNAUTHORIZED)

        group = get_object_or_404(Group, pk=pk)

        group.users_on_group.add(request.user.id)

        group.save()

        user = UserSerializer(request.user)

        return Response({'message': 'User inserted on group', 'user': user.data})

    @action(methods=['GET'], detail=False)
    def subscriptions(self, request):

        groups = Group.objects.all().filter(
            users_on_group=request.user.id)

        serializer = GroupSerializer(groups, many=True)

        return Response(serializer.data)
