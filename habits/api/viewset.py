from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializer import HabitSerializer
from habits.models import Habit
from users.models import User
import ipdb


class HabitViewSet(ModelViewSet):
        queryset = Habit.objects.all()
        serializer_class = HabitSerializer
        permission_classes = [IsAuthenticatedOrReadOnly]

        @action(methods=['GET'], detail=False)
        def personal(self, request):
            if request.user.is_anonymous:
                return Response({'error': 'Anonymous Users cannot see their personal habits'}, status=status.HTTP_401_UNAUTHORIZED)

            user = request.user._get_pk_val()

            habits = Habit.objects.filter(user=user)
            serializer = HabitSerializer(habits, many=True)

            return Response(serializer.data)

