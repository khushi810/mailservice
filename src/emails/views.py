from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from .models import Email
from .forms import EmailForm

# Create your views here.

def email_view(request):
     #  my_form = EmailForm(request.POST or None)
     #  my_form = my_form.save(commit=False)
     # # if my_form.is_valid():
     #   # my_form.save()

     #  subject = my_form.subject
     #  message = my_form.body
     #  from_email = settings.EMAIL_HOST_USER
     #  to_list = [my_form.email_to]

    my_form = EmailForm(request.POST or None)
    if my_form.is_valid():
      subject = my_form.cleaned_data['subject']
      message = my_form.cleaned_data['body']
      from_email = settings.EMAIL_HOST_USER
      email_id = my_form.cleaned_data['email_to']
      #print(email_id)
      to_list = [email_id]
      try:
        send_mail(subject, message, from_email, to_list, fail_silently=True)
      except BadHeaderError:
        return HttpResponse('Invalid header found.')
    context = {
      "form"  : my_form
    }

    return render(request, "emails/email_details.html", context)
