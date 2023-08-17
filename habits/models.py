from django.db import models


class Place(models.Model):
    place = models.CharField(max_length=100, verbose_name='Место')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Пользователь')


class Habit(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Пользователь')
    place = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name='Место')
    time = models.TimeField(auto_now_add=True, verbose_name='Время')
    action = models.CharField(max_length=100, verbose_name='Действие')
    is_pleasant = models.BooleanField(default=False, verbose_name='Приятная')
    is_related = models.BooleanField(default=False, verbose_name='Связанная')
    period = models.IntegerField(default=0, verbose_name='Период')
    reward = models.CharField(max_length=100, verbose_name='Вознаграждение')
    duration = models.IntegerField(default=0, verbose_name='Длительность в секундах')
    is_public = models.BooleanField(default=False, verbose_name='Публичный')
