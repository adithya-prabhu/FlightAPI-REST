from django.db import models

from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.dispatch import receiver

# Create your models here.
class Flight(models.Model):
    flightNumber=models.CharField(max_length=20,null=True)
    operatingcity=models.CharField(max_length=20)
    departurecity=models.CharField(max_length=20,blank=True,null=True)
    arrivalcity=models.CharField(max_length=20)
    dateofdeparture=models.DateField()
    estimatedTimeofDeparture=models.TimeField()

    def __str__(self):
        return self.flightNumber

class Passenger(models.Model):
    firstName=models.CharField(max_length=20)
    lastName=models.CharField(max_length=20)
    middleName=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)

    def __str__(self):
        return self.firstName+" "+self.lastName
    
class Reservation(models.Model):
    flight=models.ForeignKey(Flight,on_delete=models.CASCADE)
    passenger=models.OneToOneField(Passenger,on_delete=models.CASCADE)

@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def obtaintoken(sender,instance,created,**kwargs):
    if created:
        Token.objects.create(user=instance)

