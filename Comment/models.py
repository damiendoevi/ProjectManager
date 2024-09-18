from django.db import models
from Project.models import Task
from Authentication.models import MyUser
from django.utils import timezone


class Comment(models.Model):
    message = models.CharField(max_length=500, null=False)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="comments",)
    sender = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
