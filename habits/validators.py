from datetime import timedelta

from rest_framework.serializers import ValidationError


class PleasantAndRewardValidator:
    """Проверка на отсутствие связанности привычки и наличия вознаграждения."""

    def __call__(self, value):
        if value.get('is_pleasant') is False:
            if value.get('reward') and value.get('related'):
                raise ValidationError(
                    'Приятная привычка не вознаграждается'
                )
            elif value.get('reward') is None and value.get('related') is None:
                raise ValidationError(
                    'Должна быть награда'
                )


class DurationValidator:
    def __init__(self, value):
        self.value = value
        """Проверка длительности выполнения привычки"""
    def __call__(self, value):
        print(value)
        if value > 120:
            raise ValidationError(
                'Время выполнения должно быть не больше 120 секунд'
            )

        elif value == 0:
            raise ValidationError(
                'Значение должно быть больше 0'
            )


class PleasantValidator:
    """В связанные привычки могут попадать только привычки с признаком приятной привычки."""
    def __call__(self, value):
        if value.get('related') and value.get('related').is_pleasant is False:
            raise ValidationError(
                "Связанная привычка должна быть приятной"
            )


class PeriodValidator:
    """Период выполнения привычки"""
    def __call__(self, value):
        if value > 7:
            raise ValidationError(
                "Период не должен превышать 7 дней.")
        if value == 0:
            raise ValidationError(
                "Период не может быть равен 0")
        return value
