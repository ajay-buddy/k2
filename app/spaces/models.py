import uuid
from django.db import models
from django.conf import settings

# Create your models here.

class SpaceQuerySet(models.QuerySet):
    pass


class SpaceManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter()


class Space(models.Model):
    space_id     = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name         = models.CharField(max_length=100)
    description  = models.TextField(null=True, blank=True)
    created_by   = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='space_created_by')
    updated_by   = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE, related_name='space_updated_by')
    created_at   = models.DateField(auto_now_add=True)
    updated_at   = models.DateField(auto_now_add=False)

    objects = SpaceManager()

    def __str__(self):
        return self.space_id
    