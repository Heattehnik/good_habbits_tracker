from django.urls import path
from habits.apps import HabitsConfig
from rest_framework.routers import DefaultRouter
from habits.views import HabitsViewSet, PlacesViewSet

app_name = HabitsConfig.name

habits = DefaultRouter()
habits.register(r"habits", HabitsViewSet, basename="habits")
places = DefaultRouter()
places.register(r"places", PlacesViewSet, basename="places")

urlpatterns = [

] + habits.urls + places.urls
