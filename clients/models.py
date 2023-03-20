from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
import uuid
# Create your models here.
class Car(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Model = models.CharField(max_length=20)
    Raqam = models.CharField(max_length=9)
    Rang = models.CharField(max_length=15)
    Photo = models.ImageField(upload_to='images/')
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    def __str__(self):
        return str(self.Model)
        
    def get_absolute_url(self):
        return reverse('clientcars', args=[str(self.id)])
    
    # def delete(self, *args, **kwargs): 
    #     self.Photo.delete()
    #     super().delete(*args, **kwargs)



class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    transaction_id = models.CharField(max_length=100, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    cost = models.IntegerField(null=True)
    part = models.CharField(max_length=50, null=True)
    paytype = models.CharField(max_length=20, null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True)
    service = models.CharField(max_length=20, default='waiting...', editable=False, null=True)
    customer = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        null=True, 
        blank=True
    )

    def __str__(self):
        return str(self.transaction_id)



