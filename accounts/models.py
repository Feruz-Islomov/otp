from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User 
from django.urls import reverse

# Create your models here.
class CustomUser(AbstractUser):
    # balance= models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    tel = models.PositiveIntegerField(null=True, unique=True)
    shahar = models.CharField(max_length=20, null=True)
    photo = models.ImageField(upload_to='clientimages/', blank=True, null=True)
    
    USERNAME_FIELD = "tel"

    def get_absolute_url(self):
        return reverse('clientprofile', args=[])

    def __str__(self):
        return str(self.tel)
