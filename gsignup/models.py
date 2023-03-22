from django.db import models

# Create your models here.
class guide(models.Model):
    fname=models.CharField(max_length=255)
    lname=models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
    aadhar=models.CharField(max_length=255)
    email=models.CharField(max_length=255, unique=True)
    password=models.CharField(max_length=255)
