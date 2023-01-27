from django.db import models
##from django.conf import settings 
##from django.db.models.signals import post_save
##from django.dispatch import reciver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
# Create your models here.

class Restaurants(models.Model):
    name = models.CharField( max_length=50)
    vlasnik = models.ForeignKey(User,on_delete=models.CASCADE)
    cap = models.IntegerField()
    stolovi = models.IntegerField()
    opis = models.CharField(max_length=300)
    lokacija = models.CharField(max_length=30)

class Rezervacija(models.Model):
    restoran = models.ForeignKey(Restaurants,on_delete=models.CASCADE)
    br_osoba = models.IntegerField()
    datum = models.CharField(max_length=50)
    vrijeme = models.CharField(max_length=50)
#### --------
    ##@receiver(post_save, sender=settings.AUTH_USER_MODEL)
    ##def create_auth_token(sender,instance=None, created=False,**kwargs):
        ##if created:
            ##Token.objects.create(user=instance)
        
