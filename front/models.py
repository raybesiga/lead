from django.db import models
from phone_field import PhoneField

# Create your models here.

class Lead(models.Model):
    name =  models.CharField(max_length=100)
    phone_number = PhoneField(blank=True)
    email = models.EmailField()
    message = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)