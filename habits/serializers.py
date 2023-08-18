from rest_framework import serializers
from habits.models import Habit, Place


class HabitSerializer(serializers.ModelSerializer):
    """
    Serializer for Habit model
    """
    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        habit = Habit.objects.create(**validated_data)
        return habit

    class Meta:
        model = Habit
        fields = '__all__'


class PlacesSerializer(serializers.ModelSerializer):
    """
    Serializer for Places model
    """
    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        place = Place.objects.create(**validated_data)
        return place

    class Meta:
        model = Place
        fields = '__all__'
