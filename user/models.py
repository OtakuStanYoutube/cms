from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin)

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    username = models.CharField(max_length=255, unique=True, db_index=True)
    imgUrl = models.CharField(max_length=255, default='https://www.gravatar.com/avatar/00000000000000000000000000000000?d=mp&f=y')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email