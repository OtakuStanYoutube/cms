from django.db import models
from helpers.models import BaseModel

# Create your models here.
class Sponsors(BaseModel):
    SPONSOR_CATEGORY = (
        ('Sponsored', 'Sponsored'),
        ('Integrated', 'Integrated'),
        ('Dedicated', 'Dedicated'),
    )
    
    SPONSORED_DOMAIN = (
        ('Youtube', 'Youtube'),
        ('Podcast', 'Podcast'),
        ('Website', 'Website'),
    )
    name = models.CharField(max_length=100, db_index=True)
    description = models.TextField()
    domain = models.URLField(blank=True)
    sponsor_type = models.CharField(max_length=100, choices=SPONSOR_CATEGORY, db_index=True)
    sponsored_domain = models.CharField(max_length=100, choices=SPONSORED_DOMAIN, db_index=True)
    amount = models.IntegerField(default=0)

    def __str__(self):
        return self.name