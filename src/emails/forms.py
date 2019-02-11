from django import forms

from .models import Email


class EmailForm(forms.ModelForm):
  class Meta:
    model = Email
    fields = [
        'email_to',
        'cc',
        'bcc',
        'subject',
        'body'
    ]
