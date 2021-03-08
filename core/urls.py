from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.api.viewset import UserViewSet
from groups.api.viewset import GroupViewSet
from habits.api.viewset import HabitViewSet
from activities.api.viewset import ActivityViewSet
from goals.api.viewset import GoalViewSet

router = routers.DefaultRouter()

router.register(r'users', UserViewSet, basename='User')
router.register(r'habits', HabitViewSet, basename='Habit')

router.register(r'groups', GroupViewSet, basename='Group')
router.register(r'activities', ActivityViewSet, basename='Activity')
router.register(r'goals', GoalViewSet, basename='Goal')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('sessions/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('refresh-token/', TokenRefreshView.as_view(), name='token_refresh')
]
