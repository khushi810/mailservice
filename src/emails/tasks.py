from __future__ import absolute_import, unicode_literals
from celery import task
from .models import Email
from django.utils import timezone

import logging
logger = logging.getLogger(__name__)

@task()
def scheduled_email_report():
  time_range = timezone.now() - timezone.timedelta(minutes=30)
  objects = Email.objects.filter(created_at__gte=time_range)
  print(objects)
