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
   
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    review_count = models.CharField(max_length=100)
    subscription_id = models.ForeignKey(Subscription, related_name='users', on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        User.objects.create(user=instance)
    instance.profile.save()