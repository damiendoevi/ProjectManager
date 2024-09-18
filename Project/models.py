from django.db import models
from Authentication.models import MyUser

class Project(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)
    code_invitation = models.CharField(max_length=255, unique=True);
    admin = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name="projects",)
    members = models.ManyToManyField(MyUser);

    
class Task(models.Model):
    STATUS_CHOICE = [
        ("TODO", "To do"),
        ("PENDING", "Pending"),
        ("DONE", "Done"),
    ];
    PRIORITY_CHOICE = [
        ("LOW", "Low"),
        ("MEDIUM", "Medium"),
        ("HIGH", "Hight"),
    ];


    title = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=500, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="tasks",)
    status = models.CharField(max_length=7, choices=STATUS_CHOICE, default="TODO");
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICE, default="LOW");
    start_date = models.DateTimeField(null=True);
    end_date = models.DateTimeField();
    members = models.ManyToManyField(MyUser);

    class Meta:
        unique_together = ['title', 'project']



