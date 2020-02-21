import uuid
from django.db import models
from django.conf import settings

from project.models import Project
from spaces.models import Space

# Create your models here.

class BoardQuerySet(models.QuerySet):
    pass


class BoardManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter()


class Board(models.Model):
    board_id   = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name         = models.CharField(max_length=100)
    description  = models.TextField(null=True, blank=True)
    # space_id     = models.ForeignKey(Space, on_delete=models.CASCADE, null=True, related_name='board_belongs_to_space')
    project_id   = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, related_name='board_belongs_to_project')
    created_by   = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='Board_created_by')
    updated_by   = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE, related_name='board_updated_by')
    created_at   = models.DateField(auto_now_add=True)
    updated_at   = models.DateField(auto_now_add=False)

    objects = BoardManager()

    def __str__(self):
        return self.board_id
    