from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Profile(models.Model):
    user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    telegram = models.CharField(max_length=50, null=True, blank=True)
    vk = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    nikname = models.CharField(max_length=50, null=True, blank=True)
    civilname = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.user)
