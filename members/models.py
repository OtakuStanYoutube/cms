from django.db import models
from helpers.models import BaseModel

# Create your models here.
class Members(BaseModel):
    DESIGNATION_CHOICES = (
        ('Video Editor', 'Video Editor'),
        ('Narrator', 'Narrator'),
        ('Script Writer', 'Script Writer'),
        ('Software Engineer', 'Software Engineer'),
        ('Others', 'Others'),
    )
    name = models.CharField(max_length=250, db_index=True)
    imgUrl = models.CharField(max_length=255, default='https://www.gravatar.com/avatar/00000000000000000000000000000000?d=mp&f=y')
    designation = models.CharField(max_length=250, choices=DESIGNATION_CHOICES, default='Others', db_index=True)
    profile_link = models.CharField(max_length=255, default='#')
    
    def __str__(self):
        return self.name