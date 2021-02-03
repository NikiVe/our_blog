from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from . managers import MyUserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


# Custom user model class
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email'), max_length=80, unique=True)
    first_name = models.CharField(_('first_name'), max_length=50, blank=True)
    last_name = models.CharField(_('last_name'), max_length=50, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = MyUserManager()

    def __str__(self):
        return self.email

    @property
    def full_name(self):
        return f'{first_name} {last_name}'

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
