from django.db.models.signals import post_save  # event for a save event in the db.
from django.contrib.auth.models import User
from django.dispatch import receiver            # to recieve an event
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()