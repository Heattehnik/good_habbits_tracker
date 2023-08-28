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

    def validate(self, data):
        related = data.get("related")
        reward = data.get("reward")
        is_pleasant = data.get("is_pleasant")
        if related and reward:
            raise serializers.ValidationError(
                "Связанная привычка и вознаграждение не могут быть указаны одновременно"
            )
        elif is_pleasant and (reward is not None or related is not None):
            raise serializers.ValidationError(
                "У приятной привычки не может быть вознаграждения или связанной привычки!"
            )
        return data

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
