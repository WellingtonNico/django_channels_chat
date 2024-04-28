from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class Usuario(AbstractUser):
    username = None
    nome = models.CharField(max_length=60)
    email = models.EmailField(_("email address"), unique=True)
    REQUIRED_FIELDS = ["nome"]
    USERNAME_FIELD = "email"

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        abstract = False
