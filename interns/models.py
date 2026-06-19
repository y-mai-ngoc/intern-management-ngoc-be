from django.db import models

class Intern(models.Model):
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Completed', 'Completed'),
        ('Paused', 'Paused'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    university = models.CharField(max_length=255)
    major = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    photo = models.URLField(max_length=500, blank=True, null=True)

    start_date = models.DateField(blank=True, null=True)
    mentor = models.CharField(max_length=255, default="Lead Mentor")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Active')
    attendance_rate = models.PositiveSmallIntegerField(
        default=100,
        help_text="Tỷ lệ điểm danh (%), mentor tự nhập, 0-100"
    )
    skill_growth = models.DecimalField(
        max_digits=3, decimal_places=1, default=0.0,
        help_text="Điểm đánh giá kỹ năng, thang 0.0 - 10.0"
    )
    skill_growth_delta = models.DecimalField(
        max_digits=3, decimal_places=1, default=0.0, blank=True,
        help_text="Chênh lệch so với lần đánh giá trước, vd +1.2 hoặc -0.5"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class LearningRecord(models.Model):
    STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('in_progress', 'In Progress'),
        ('not_started', 'Not Started'),
    ]

    intern = models.ForeignKey(Intern, related_name='learning_records', on_delete=models.CASCADE)
    topic = models.CharField(max_length=255)
    desc = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not_started')
    date = models.DateField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.topic} - {self.intern.name}"


class WeeklyTask(models.Model):
    intern = models.ForeignKey(Intern, related_name='weekly_tasks', on_delete=models.CASCADE)
    week = models.CharField(max_length=50, default='Week 1: June 22 - June 28')
    name = models.CharField(max_length=255)
    desc = models.TextField(blank=True)
    mon = models.CharField(max_length=10, blank=True, default='')
    tue = models.CharField(max_length=10, blank=True, default='')
    wed = models.CharField(max_length=10, blank=True, default='')
    thu = models.CharField(max_length=10, blank=True, default='')
    fri = models.CharField(max_length=10, blank=True, default='')
    result = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.intern.name}"