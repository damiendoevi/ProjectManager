from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, email, last_name, first_name, password=None, is_staff=None):
        user = self.model(
            last_name = last_name,
            first_name = first_name,
            email=self.normalize_email(email),
        )

        if is_staff:
            user.is_staff = True

        user.set_password(password)
        user.save()

        return user
        
        
    def create_superuser(self, email, last_name, first_name, password=None):
        user = self.create_user(email, last_name, first_name, password, is_staff=True)

        return user
    

class MyUser(AbstractBaseUser, PermissionsMixin):
    last_name = models.CharField(max_length=50, null=False)
    first_name = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=255, unique=True, null=False)
    date_joined = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False);
    is_active = models.BooleanField(default=True);
    
    REQUIRED_FIELDS = ['last_name', 'first_name']
    USERNAME_FIELD = "email"

    objects = MyUserManager()

    class Meta:
        unique_together = ['last_name', 'first_name']