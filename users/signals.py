from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# signal gets fired when post_saved is called


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
  # run everytime a user is created
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
  # run everytime a user is saved or updated
    instance.profile.save()
