from __future__ import absolute_import, unicode_literals
from celery import task
from .models import Email, Admin
from django.utils import timezone
import csv
from django.core import serializers
from django.core.mail import EmailMessage
import itertools

import logging
logger = logging.getLogger(__name__)

@task()
def scheduled_email_report():
  time_range = timezone.now() - timezone.timedelta(minutes=30)
  objects = Email.objects.filter(created_at__gte=time_range)
  field_names = ['id', 'email_to', 'cc', 'bcc', 'subject', 'body', 'created_at']
  export_as_csv(objects, field_names)
  file = open('/tmp/emails_dump.csv')
  admin_emails = list(itertools.chain(*list(Admin.objects.values_list('email'))))
  message = EmailMessage(
    'Email Report',
    'Please find attached CSV containing emails sent in last 30 mins',
    'help@mailservice.com',
    admin_emails,
    reply_to=[admin_emails[0]]
  )
  message.attach_file('/tmp/emails_dump.csv', mimetype='text/csv')
  message.send()


def export_as_csv(emails, fields):
  print(emails)
  with open('/tmp/emails_dump.csv', 'w', newline="") as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
    fields = list(fields) # loses order, but at least it's consistent
    writer.writerow(fields)
    for email in emails:

      serialized_obj = serializers.serialize('json', [ email, ])
      print(serialized_obj)
      row = []
      for field in fields:
        row.append(getattr(email, field))
      print(row)
      writer.writerow(row)
