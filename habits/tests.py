from users.models import User
from rest_framework.test import APITestCase
from rest_framework.request import Request
from .serializers import HabitSerializer
from .models import Habit


class HabitSerializerTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            email='testuser@mail.ru',
            password='testpassword'
        )
        self.serializer_context = {'request': Request(user=self.user)}
        self.client.force_authenticate(user=self.user)
        self.validated_data = {
            'place': 1,
            'time': '12:00:00',
            'action': 'Some Action',
            'is_pleasant': False,
            'is_related': False,
            'period': 7,
            'reward': 'Some Reward',
            'duration': 60,
            'is_public': False
        }

    def test_create_habit(self):
        serializer = HabitSerializer(context=self.serializer_context)
        habit = serializer.create(self.validated_data)

        self.assertEqual(habit.user, self.user)
        self.assertEqual(habit.place, self.validated_data['place'])
        self.assertEqual(habit.time.strftime('%H:%M:%S'),
                         self.validated_data['time'])
        self.assertEqual(habit.action, self.validated_data['action'])
        self.assertEqual(habit.is_pleasant, self.validated_data['is_pleasant'])
        self.assertEqual(habit.is_related, self.validated_data['is_related'])
        self.assertEqual(habit.period, self.validated_data['period'])
        self.assertEqual(habit.reward, self.validated_data['reward'])
        self.assertEqual(habit.duration, self.validated_data['duration'])
        self.assertEqual(habit.is_public, self.validated_data['is_public'])
