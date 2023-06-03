from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_save

from role_based_auth_core.utils import slug_pre_save_receiver


class accountsRole(models.Model):
    name = models.CharField(max_length=50, unique=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, null=True, blank=True, unique=True)

    def __str__(self):
        return self.name


pre_save.connect(slug_pre_save_receiver, sender=accountsRole)


class User(AbstractUser):
    role = models.ForeignKey(accountsRole, on_delete=models.CASCADE, null=True, blank=True, related_name="user_role")
    updated_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, null=True, blank=True, unique=True)

    def __str__(self):
        return self.username


pre_save.connect(slug_pre_save_receiver, sender=User)
