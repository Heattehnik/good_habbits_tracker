from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from habits.models import Habit, Place
from habits.paginators import HabitsPaginator, PlacesPaginator
from habits.serializers import HabitSerializer, PlacesSerializer


class HabitsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited habits.
    """
    serializer_class = HabitSerializer
    pagination_class = HabitsPaginator
    queryset = Habit.objects.all()


class PlacesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited places.
    """
    serializer_class = PlacesSerializer
    pagination_class = PlacesPaginator
    queryset = Place.objects.all()
    permission_classes = [IsAuthenticated]
