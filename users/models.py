import uuid

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django_countries.fields import CountryField


class CustomUser(AbstractUser):
    pass


class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bio = models.CharField(max_length=600, blank=True)
    location = models.CharField(max_length=200, blank=True)
    country = CountryField(blank_label='(select country)')
    birth_date = models.DateField(null=True, blank=True)
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='profile')

    def __str__(self):
        return self.bio

    def get_absolute_url(self):
        return reverse('profile_detail', args=[str(self.id)])


@receiver(post_save, sender=get_user_model())
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=get_user_model())
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
