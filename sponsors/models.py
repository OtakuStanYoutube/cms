from django.db import models
from helpers.models import BaseModel

# Create your models here.
class Sponsors(BaseModel):
    CATEGORY = (
        ('Sponsored', 'Sponsored'),
        ('Integrated', 'Integrated'),
        ('Dedicated', 'Dedicated'),
    )
    name = models.CharField(max_length=100)
    description = models.TextField()
    domain = models.URLField(blank=True)
    sponsor_type = models.CharField(max_length=100, choices=CATEGORY)
    amount = models.IntegerField(default=0)

    def __str__(self):
        return self.name