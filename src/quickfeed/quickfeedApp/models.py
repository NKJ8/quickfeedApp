from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Plan(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    validity = models.CharField(max_length=100)
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

class Subscription(models.Model):
    plan_id = models.ForeignKey(Plan, related_name='subscriptions', on_delete=models.SET_NULL, null=True)
    from_date = models.DateTimeField()
    to_date = models.DateTimeField()
   
class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    review_count = models.CharField(max_length=100)
    subscription_id = models.ForeignKey(Subscription, related_name='users', on_delete=models.SET_NULL, null=True)




@receiver(post_save, sender=User)
def create_User_profile(sender, instance, created, **kwargs):
    if created:
        Users.objects.create(user=instance).save()
   
#post_save.connect(create_User_profile, sender=User)