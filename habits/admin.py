from django.contrib import admin
from habits.models import Habit


@admin.register(Habit)
class AdminHabit(admin.ModelAdmin):
    pass
