from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .manager import UserManager

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='User email ', max_length=255, unique=True)
    name = models.CharField(verbose_name='User name', max_length=255, auto_created=True, blank=True)
    
    is_staff = models.BooleanField(verbose_name='Is staff', default=False, blank=True)
    is_superuser = models.BooleanField(verbose_name='Is superuser', default=False)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']
    
    def __str__(self) -> str:
        return str(self.email)
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['id', 'email']
