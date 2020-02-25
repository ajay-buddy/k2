from django.db import models
from django.conf import settings

# Create your models here.

class KTagsQuerySet(models.QuerySet):
    pass


class KTagsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter()


class KTags(models.Model):
    ktag_id      = models.AutoField(primary_key=True, editable=False)
    name         = models.CharField(max_length=100)
    description  = models.TextField(null=True, blank=True)
    created_by   = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ktags_created_by')
    updated_by   = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE, related_name='ktags_updated_by')
    created_at   = models.DateField(auto_now_add=True)
    updated_at   = models.DateField(auto_now_add=False)

    objects = KTagsManager()

    def __str__(self):
        return self.name
    