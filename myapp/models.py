from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class signup(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    emailid=models.EmailField(max_length=100)
    phoneno=models.CharField(max_length=10)
    password=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    zipcode=models.IntegerField()

    def __str__(self):
        return self.fname

class bookvehicle(models.Model):
    pickup=models.CharField(max_length=100)
    drop=models.CharField(max_length=100)
    truck=models.CharField(max_length=100)

    def __str__(self):
        return self.pickup


class proceed(models.Model):
    pickuplocation=models.CharField(max_length=100)
    droplocation=models.CharField(max_length=100)
    trucktype=models.CharField(max_length=100)
    labour=models.CharField(max_length=10, default='')
    pickupdate=models.CharField(max_length=100)
    goodstype=models.CharField(max_length=100)
    weight=models.IntegerField()
    
    def __str__(self):
        return self.pickupdate

class summary(models.Model):
    pickuplocation=models.CharField(max_length=100)
    droplocation=models.CharField(max_length=100)
    trucktype=models.CharField(max_length=100)
    labour=models.CharField(max_length=10, default='')
    pickupdate=models.CharField(max_length=100)
    goodstype=models.CharField(max_length=100)
    weight=models.IntegerField()

    def __str__(self):
        return self.pickupdate


class contactus(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    mno=models.IntegerField()
    msg=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class driver(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    phonnumber=models.IntegerField()
    licensenumber=models.CharField(max_length=14)
    address=models.CharField(max_length=100)

    def __str__(self):
        return self.first_name

class trucks(models.Model):
    truck_name=models.CharField(max_length=20)
    truck_type=models.CharField(max_length=20)
    registration_number=models.CharField(max_length=20)
    owner_name=models.CharField(max_length=20)
    owner_mobile_number=models.IntegerField()
    
    def __str__(self):
        return self.truck_name

class payment(models.Model):
    cardnumber=models.IntegerField()
    holdername=models.CharField(max_length=20)
    exp_month=models.IntegerField()
    exp_year=models.IntegerField()
    cvv=models.IntegerField()

    def __str__(self):
        return self.cardnumber

class Transaction(models.Model):
    made_on = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    order_id = models.CharField(unique=True, max_length=100, null=True, blank=True)
    checksum = models.CharField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.order_id is None and self.made_on and self.id:
            self.order_id = self.made_on.strftime('PAY2ME%Y%m%dODR') + str(self.id)
        return super().save(*args, **kwargs)