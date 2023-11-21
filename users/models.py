from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager


USER_ROLES = (
    ('admin', 'admin'),
    ('customer', 'customer'),
    ('manager', 'manager'),
)


class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, default="username"+timezone.now().strftime("%M"))
    email = models.EmailField(_("email address"), unique=True)
    phone = models.CharField(max_length=20, default="+998999999999")
    roles = models.CharField(choices=USER_ROLES, max_length=20)
    contracts = models.IntegerField(default=0)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["password"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email



