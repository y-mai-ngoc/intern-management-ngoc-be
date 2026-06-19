from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InternViewSet, LearningRecordViewSet, WeeklyTaskViewSet

router = DefaultRouter()
router.register(r'interns', InternViewSet, basename='intern')
router.register(r'learning-records', LearningRecordViewSet, basename='learningrecord')
router.register(r'weekly-tasks', WeeklyTaskViewSet, basename='weeklytask')

urlpatterns = [
    path('', include(router.urls)),
]
