from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser, PermissionsMixin)

# Create your models here.

class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None):
        if username is None:
            raise TypeError('Users should have a username')
        if email is None:
            raise TypeError('Users should have a Email')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None):
        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user(username, email, password)
        user.role = 'Admin'
        user.is_active = True
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

class User(AbstractBaseUser, PermissionsMixin):
    CATEGORY = (
        ('Admin', 'Admin'),
        ('Editor', 'Editor'),
        ('Viewer', 'Viewer'),
    )
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    username = models.CharField(max_length=255, unique=True, db_index=True)
    imgUrl = models.CharField(max_length=255, default='https://www.gravatar.com/avatar/00000000000000000000000000000000?d=mp&f=y')
    role = models.CharField(max_length=200, null=True, choices=CATEGORY)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email