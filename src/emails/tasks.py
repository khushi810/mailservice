""" Instructions
Run below command to run celery worker process which processes email report
every 30 minutes.

celery -A mailservice worker -l info -B

Redis is used by celery as broker
Install redis (LINUX - sudo apt install redis | MacOS - brew install redis)
"""

from __future__ import absolute_import, unicode_literals
from celery import task
from .models import Email, Admin
from django.utils import timezone
import csv
from django.core.mail import EmailMessage
import itertools
import logging
logger = logging.getLogger(__name__)

# Create and export log file for admin to send
@task()
def scheduled_email_report():
  time_range = timezone.now() - timezone.timedelta(minutes=30)
  objects = Email.objects.filter(created_at__gte=time_range)
  # If no email sent in last 30 mins, there is no need to send email report.
  if not objects:
    logger.info("No emails found in last 30 minutes")
    return
  field_names = ['id', 'email_to', 'cc', 'bcc', 'subject', 'body', 'created_at']
  export_as_csv(objects, field_names)
  file = open('/tmp/emails_dump.csv')
  admin_emails = list(itertools.chain(*list(Admin.objects.values_list('email'))))
  logger.info("Sending mails to Admins:" + ", ".join(admin_emails))
  message = EmailMessage(
    'Email Report',
    'Please find attached CSV containing emails sent in last 30 mins',
    'help@mailservice.com',
    admin_emails,
    reply_to=[admin_emails[0]]
  )
  message.attach_file('/tmp/emails_dump.csv', mimetype='text/csv')
  message.send()
  logger.info("Email report sent successfully")


# Build CSV for emails sent in last 30 mins
def export_as_csv(emails, fields):
  with open('/tmp/emails_dump.csv', 'w', newline="") as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
    fields = list(fields) # loses order, but at least it's consistent
    writer.writerow(fields)
    for email in emails:
      row = []
      for field in fields:
        row.append(getattr(email, field))
      writer.writerow(row)
