from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()

class Profile(models.Model):
    user=models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    telegram = models.CharField(max_length=50, null=True, blank=True)
    vk = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    nikname = models.CharField(max_length=50, null=True, blank=True)
    civilname = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.user)

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    print(instance)
    if created:
        Profile.objects.create(user=instance)
