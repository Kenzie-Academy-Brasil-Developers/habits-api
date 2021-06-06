from rest_framework.viewsets import ModelViewSet
from .serializer import UserSerializer
from django.contrib.auth.models import User as DjangoUser
from users.models import User
from rest_framework.response import Response
from rest_framework import status


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            User.objects.create_user(
                **request.data
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None, *args, **kwargs):
        user = User.objects.get(pk=pk)

        pk = int(pk)

        if pk != request.user.id:
            return Response({
                'status': 'error',
                'message': 'Only the owner of the profile can update his own information'},
                status=status.HTTP_401_UNAUTHORIZED)

        serializer = self.serializer_class(
            user, data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
