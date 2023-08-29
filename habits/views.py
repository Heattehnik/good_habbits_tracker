from rest_framework import viewsets
from django.db.models import Q

from habits.models import Habit, Place
from habits.paginators import HabitsPaginator, PlacesPaginator
from habits.permissions import IsOwner, IsPublic
from habits.serializers import HabitSerializer, PlacesSerializer
from habits.services import set_schedule


class HabitsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited habits.
    """

    serializer_class = HabitSerializer
    pagination_class = HabitsPaginator
    queryset = Habit.objects.all()
    permission_classes = [IsOwner, IsPublic]

    def get_queryset(self):
        return Habit.objects.filter(
            Q(user=self.request.user) | Q(is_public=True)
        )

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.creator = self.request.user
        new_habit.save()
        set_schedule(new_habit)


class PlacesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited places.
    """

    serializer_class = PlacesSerializer
    pagination_class = PlacesPaginator
    queryset = Place.objects.all()
    permission_classes = [IsOwner]
