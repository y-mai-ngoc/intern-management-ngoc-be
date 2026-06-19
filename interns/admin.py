from django.contrib import admin
from .models import Intern, LearningRecord, WeeklyTask


@admin.register(Intern)
class InternAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'email', 'company', 'status', 'created_at')
	search_fields = ('name', 'email', 'company', 'university')


@admin.register(LearningRecord)
class LearningRecordAdmin(admin.ModelAdmin):
	list_display = ('id', 'topic', 'intern', 'status', 'date')
	search_fields = ('topic', 'intern__name')


@admin.register(WeeklyTask)
class WeeklyTaskAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'intern')
	search_fields = ('name', 'intern__name')
