from django.db import models
from clients.models import Order, Car
from django.contrib.auth import get_user_model
import uuid
from accounts.models import CustomUser

class Driver_cart_order(models.Model):
    PENDING = 'pending'
    FINISHED = 'finished'
    STATUS = [
        (PENDING, 'pending'),
        (FINISHED, 'finished'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cost = models.IntegerField(null=True)
    part = models.CharField(max_length=50, null=True)
    paytype = models.CharField(max_length=50, null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True)   
    ordered_by = models.CharField(max_length=60, null=True)
    service = models.CharField(max_length=20, null=True, choices=STATUS, default=PENDING)
    driver = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return str(self.date_ordered)
    
    # @property
    # def get_cart_total(self):
    #     orderitems = self.orderitem_set.all()
    #     total = sum([item.get_total for item in orderitems])
    #     return total

    # @property
    # def get_total(self):
    #     total = self.quantity * self.product.price
    #     return total

class Balance(models.Model):
    balance = models.IntegerField(null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return str(self.balance)

    
    