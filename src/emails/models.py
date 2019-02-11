from django.db import models

# Create your models here.

class Admin(models.Model):
  username    = models.CharField(max_length=100)
  password    = models.CharField(max_length=50)

class Email(models.Model):
  subject       = models.CharField(max_length=120)
  body          = models.TextField()
  cc            = models.CharField(max_length=120)
  bcc           = models.CharField(max_length=120)
  emailid_from  = models.CharField(max_length=120)
  emailid_to    = models.CharField(max_length=120)

#class CSV(models.Model):
