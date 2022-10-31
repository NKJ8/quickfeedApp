
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User


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
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    username = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    dob = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    review_count = models.CharField(max_length=100, null=True)
    subscription_id = models.ForeignKey(Subscription, related_name='users', on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f"{self.name} {self.email}"

class Service(models.Model):
    description = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    category_id = models.ForeignKey(Category, related_name='category', on_delete=models.SET_NULL, null=True)
    price = models.CharField(max_length=20)
    tags = models.CharField(max_length=20)
    time_required = models.CharField(max_length=20)

class Business(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    zipcode = models.CharField(max_length=100, null=True)
    is_open = models.BooleanField(max_length=100, null=True)
    description = models.CharField(max_length=1000, null=True)
    review_count = models.CharField(max_length=100, null=True)
    # service_id = models.ForeignKey(Service, related_name='card_details', on_delete=models.SET_NULL, null=True)
    subscription_id = models.ForeignKey(Subscription, related_name='business', on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

class CardDetails(models.Model):
    card_number = models.CharField(max_length=20)
    card_exp_month = models.CharField(max_length=2)
    card_exp_year = models.CharField(max_length=4)
    user_id = models.ForeignKey(User, related_name='card_details', on_delete=models.SET_NULL, null=True)

class Reviews(models.Model):
    review = models.CharField(max_length=20)
    user_id = models.ForeignKey(User, related_name='users', on_delete=models.SET_NULL, null=True)
    business_id = models.ForeignKey(Business, related_name='reviews', on_delete=models.SET_NULL, null=True)
    anonymous = models.BooleanField(default=False)
    date = models.DateTimeField()

class Profile(models.Model):
    business_id = models.ForeignKey(Business, related_name='profile', on_delete=models.SET_NULL, null=True)
    total_reviews = models.CharField(max_length=20)
    total_like = models.CharField(max_length=20)
    total_ratings = models.CharField(max_length=20)
    total_customers = models.CharField(max_length=20)    





