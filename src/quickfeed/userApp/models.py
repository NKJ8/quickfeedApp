from django.db import models

from quickfeed.quickfeedApp.models import Subscription

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    review_count = models.CharField(max_length=100)
    subscription_id = models.ForeignKey(Subscription, related_name='users', on_delete=models.SET_NULL, null=True)