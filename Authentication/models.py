from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from django.contrib.auth.base_user import AbstractBaseUser

class MyUser(AbstractBaseUser, PermissionsMixin):
    last_name = models.CharField(max_length=50, null=False)
    first_name = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=255, unique=True, null=False)
    date_joined = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False);
    is_active = models.BooleanField(default=True);
    
    REQUIRED_FIELDS = ['last_name', 'first_name']
    USERNAME_FIELD = "email"

    class Meta:
        unique_together = ['last_name', 'first_name']