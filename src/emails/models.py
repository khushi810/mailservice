from django.db import models
from django.utils import timezone
#For admin
class Admin(models.Model):
  username    = models.CharField(max_length=100)
  password    = models.CharField(max_length=50)
  email       = models.EmailField()

# For Email
class Email(models.Model):
  email_to      = models.CharField(max_length=120)
  cc            = models.CharField(max_length=120, null=True)
  bcc           = models.CharField(max_length=120, null=True)
  subject       = models.CharField(max_length=120)
  body          = models.TextField()
  created_at    = models.DateTimeField(editable=False)
  updated_at    = models.DateTimeField()

  def save(self, *args, **kwargs):
    ''' On save, update timestamps '''
    if not self.id:
      self.created_at = timezone.now()
      self.updated_at = timezone.now()
    return super(Email, self).save(*args, **kwargs)

