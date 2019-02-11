from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from .models import Email
from .forms import EmailForm

# Create your views here.

def email_view(request):

    my_form = EmailForm(request.POST or None)
    if my_form.is_valid():
      subject = my_form.cleaned_data['subject']
      message = my_form.cleaned_data['body']
      from_email = settings.EMAIL_HOST_USER
      email_id = my_form.cleaned_data['email_to']
      to_list = [email_id]
      my_form.save()

      try:
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        my_form = EmailForm()
      except BadHeaderError:
        return HttpResponse('Invalid header found.')
    context = {
      "form"  : my_form
    }

    return render(request, "emails/email_details.html", context)
