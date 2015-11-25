from django.db import models
from django.contrib.auth.models import AbstractUser

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.


class MyUser(AbstractUser):
    GENDER_CHOICE = (('M', 'Male'), ('F', 'Female'), ('NS', 'Not Specified'))
    tag_line = models.CharField(max_length=100, default="")
    gender = models.CharField(max_length=2, choices=GENDER_CHOICE, default=GENDER_CHOICE[2][0])
    age = models.IntegerField(null=True, blank=True)


@receiver(post_save, sender=MyUser)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        print(instance)
        Token.objects.create(user=instance)
