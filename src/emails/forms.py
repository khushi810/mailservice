from django import forms

from .models import Email


class EmailForm(forms.ModelForm):

  cc = forms.CharField(required=False)
  bcc = forms.CharField(required=False)

  class Meta:
    model = Email
    fields = [
        'email_to',
        'cc',
        'bcc',
        'subject',
        'body'
    ]
