from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from project.models import Project
from spaces.models import Space
from board.models import Board
from task.models import Task
from ktags.models import KTags
# Create your models here.

class KInstanceQuerySet(models.QuerySet):
    pass


class KInstanceManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter()


class KInstance(models.Model):
    kinstance_id = models.AutoField(primary_key=True, editable=False)
    name         = models.CharField(max_length=100, blank=True, null=True)
    project_id   = models.CharField(max_length=100, blank=True, null=True)
    space_id     = models.CharField(max_length=100, blank=True, null=True)
    board_id     = models.CharField(max_length=100, blank=True, null=True)
    task_id      = models.CharField(max_length=100, blank=True, null=True)
    comment_id   = models.CharField(max_length=100, blank=True, null=True)
    instance_type= models.CharField(max_length=100, blank=True, null=True)
    description  = models.TextField(null=True, blank=True)
    created_by   = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='kinstance_created_by')
    updated_by   = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE, related_name='kinstance_updated_by')
    created_at   = models.DateField(auto_now_add=True)
    updated_at   = models.DateField(auto_now_add=False)

    objects = KInstanceManager()

    def __str__(self):
        return self.name


def save_KInstance_project(sender, instance, created, **kwargs):
    if created:
        KInstance.objects.create(
                project_id = instance.project_id,
                instance_type = 'project',
                description = 'project',
                name = 'project',
                created_by = instance.created_by,
                created_at = instance.created_at,
                updated_by = instance.updated_by,
                updated_at = instance.updated_at
            )

def save_KInstance_space(sender, instance, created, **kwargs):
    if created:
        KInstance.objects.create(
                space_id = instance.space_id,
                instance_type = 'space',
                description = 'space',
                name = 'space',
                created_by = instance.created_by,
                created_at = instance.created_at,
                updated_by = instance.updated_by,
                updated_at = instance.updated_at
            )
def save_KInstance_board(sender, instance, created, **kwargs):
    if created:
        KInstance.objects.create(
                board_id = instance.board_id,
                instance_type = 'board',
                description = 'board',
                name = 'board',
                created_by = instance.created_by,
                created_at = instance.created_at,
                updated_by = instance.updated_by,
                updated_at = instance.updated_at
            )
def save_KInstance_task(sender, instance, created, **kwargs):
    if created:
        KInstance.objects.create(
                task_id = instance.task_id,
                instance_type = 'task',
                description = 'task',
                name = 'task',
                created_by = instance.created_by,
                created_at = instance.created_at,
                updated_by = instance.updated_by,
                updated_at = instance.updated_at
            )
def save_KInstance_comment(sender, instance, created, **kwargs):
    if created:
        KInstance.objects.create(
                comment_id = instance.comment_id,
                instance_type = 'comment',
                description = 'comment',
                name = 'comment',
                created_by = instance.created_by,
                created_at = instance.created_at,
                updated_by = instance.updated_by,
                updated_at = instance.updated_at
            )

def save_KInstance_ktag(sender, instance, created, **kwargs):
    if created:
        KInstance.objects.create(
                ktag_id = instance.comment_id,
                instance_type = 'ktag',
                description = 'ktag',
                name = 'ktag',
                created_by = instance.created_by,
                created_at = instance.created_at,
                updated_by = instance.updated_by,
                updated_at = instance.updated_at
            )

post_save.connect(save_KInstance_project, sender=Project)
post_save.connect(save_KInstance_space, sender=Space)
post_save.connect(save_KInstance_board, sender=Board)
post_save.connect(save_KInstance_task, sender=Task)
post_save.connect(save_KInstance_ktag, sender=KTags)
# post_save.connect(save_KInstance_comment, sender=Comment)