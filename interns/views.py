from rest_framework import viewsets
from .models import Intern, LearningRecord, WeeklyTask
from .serializers import InternSerializer, LearningRecordSerializer, WeeklyTaskSerializer


class InternViewSet(viewsets.ModelViewSet):
	queryset = Intern.objects.all().order_by('-created_at')
	serializer_class = InternSerializer


class LearningRecordViewSet(viewsets.ModelViewSet):
    serializer_class = LearningRecordSerializer

    def get_queryset(self):
        queryset = LearningRecord.objects.all().order_by('-created_at')
        intern_id = self.request.query_params.get('intern')
        if intern_id:
            queryset = queryset.filter(intern_id=intern_id)
        return queryset


class WeeklyTaskViewSet(viewsets.ModelViewSet):
    serializer_class = WeeklyTaskSerializer

    def get_queryset(self):
        queryset = WeeklyTask.objects.all().order_by('-created_at')
        intern_id = self.request.query_params.get('intern')
        if intern_id:
            queryset = queryset.filter(intern_id=intern_id)
        return queryset
