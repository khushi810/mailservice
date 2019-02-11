from django import forms

from .models import Email

# class EmailForm(forms.Form):
#     email_to      = forms.EmailField(required=True)
#     subject       = forms.CharField()
#     body          = forms.CharField(widget=forms.Textarea)


class EmailForm(forms.ModelForm):
  class Meta:
    model = Email
    fields = [
        'email_to',
        'subject',
        'body'
    ]
