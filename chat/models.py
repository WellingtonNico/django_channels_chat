from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver


User._meta.get_field("email")._unique = True
User.USERNAME_FIELD = "email"
User.REQUIRED_FIELDS = ["username"]


@receiver(pre_save, sender=User)
def preencher_username_com_email(sender, instance: User, *args, **kwargs):
    instance.username = instance.email
