from django.db import models

# Create your models here.
import uuid
from django.db import models

class ClientBinding(models.Model):
    id          = models.UUIDField(
                                    primary_key=True, 
                                    default=uuid.uuid4, 
                                    editable=False
                                    )
    client      = models.UUIDField(default=uuid.uuid4,)
    study_group = models.UUIDField(default=uuid.uuid4,)

class FeaturesBinding(models.Model):
    id          = models.UUIDField(
                                    primary_key=True, 
                                    default=uuid.uuid4, 
                                    editable=False
                                    )
    client      = models.UUIDField(default=uuid.uuid4,)
    forecast      = models.BooleanField(default=False)
    reforecast = models.BooleanField(default=False)
    portfolioView = models.BooleanField(default=False)

class MatrixBinding(models.Model):
    id          = models.UUIDField(
                                    primary_key=True, 
                                    default=uuid.uuid4, 
                                    editable=False
                                    )
    client      = models.UUIDField(default=uuid.uuid4,)
    ctms_matrix      = models.BooleanField(default=False)
    design_optimization_matrix = models.BooleanField(default=False)
    cost_matrix = models.BooleanField(default=False)