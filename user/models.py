from django.db import models
from django.contrib.auth.models import AbstractUser 
from .managers import MyUserManager

class MyUser(AbstractUser):
    username = None
    email = models.EmailField(
        verbose_name = 'email address',
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=255, default='')
    surname = models.CharField(max_length=500, default='')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password','name','surname',]

    def __str__(self):
        return self.name
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self,app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin
