from django.db import models

# Create your models here.
import uuid
from django.db import models
from django.conf import settings

from spaces.models import Space
from project.models import Project
from board.models import Board

# Create your models here.

class TaskQuerySet(models.QuerySet):
    pass


class TaskManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter()


class Task(models.Model):
    task_id      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name         = models.CharField(max_length=100)
    description  = models.TextField(null=True, blank=True)
    space_id     = models.ForeignKey(Space, on_delete=models.CASCADE, null=True, related_name='task_belongs_to_space')
    project_id   = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, related_name='task_belongs_to_project')
    board_id     = models.ForeignKey(Board, on_delete=models.CASCADE, null=True, related_name='task_belongs_to_board')
    created_by   = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='task_created_by')
    updated_by   = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE, related_name='task_updated_by')
    created_at   = models.DateField(auto_now_add=True)
    updated_at   = models.DateField(auto_now_add=False)

    objects = TaskManager()

    def __str__(self):
        return self.task_id
    