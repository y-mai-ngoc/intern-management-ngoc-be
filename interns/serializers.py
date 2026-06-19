from rest_framework import serializers
from .models import Intern, LearningRecord, WeeklyTask

class LearningRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningRecord
        fields = ['id', 'intern', 'topic', 'desc', 'status', 'date', 'created_at']

class WeeklyTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeeklyTask
        fields = ['id', 'intern', 'week', 'name', 'desc', 'mon', 'tue', 'wed', 'thu', 'fri', 'result', 'created_at']

class InternSerializer(serializers.ModelSerializer):
    learning_records = LearningRecordSerializer(many=True, read_only=True)
    weekly_tasks = WeeklyTaskSerializer(many=True, read_only=True)

    class Meta:
        model = Intern
        fields = [
            'id',
            'name',
            'email',
            'university',
            'major',
            'company',
            'photo',
            'start_date',
            'mentor',
            'status',
            'attendance_rate',
            'skill_growth',
            'skill_growth_delta',
            'created_at',
            'learning_records',
            'weekly_tasks',
        ]
