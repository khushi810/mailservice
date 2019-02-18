from django.db import models

class Admin(models.Model):
  username    = models.CharField(max_length=100)
  password    = models.CharField(max_length=50)

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
      self.created = timezone.now()
    self.modified = timezone.now()
    return super(User, self).save(*args, **kwargs)

