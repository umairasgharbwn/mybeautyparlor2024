from django.db import models

# Create your models here.

class contactEnquiry(models.Model):
    name=models.CharField(max_length=50)
    email_adress=models.CharField(max_length=60)
    Phone=models.CharField(max_length=50)
    category=models.CharField(max_length=50)
    Date=models.CharField(max_length=60)
    message=models.CharField(max_length=100)
