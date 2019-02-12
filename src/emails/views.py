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
      cc = my_form.cleaned_data['cc']
      bcc = my_form.cleaned_data['bcc']
      email_id_split = tuple(email_id.split(","))
      cc_split  = tuple(cc.split(","))
      bcc_split  = tuple(bcc.split(","))
      to_list = [email_id_split]
      cc_list = [cc_split]
      bcc_list = [bcc_split]

      email = EmailMessage(
          subject=subject,
          body=message,
          from_email=from_email,
          to=to_list,
          cc=cc_list,
          bcc=bcc_list,
          reply_to=[from_email]
        )

      try:
        # TODO: Put send_mail and save() in transaction
        # send_mail(subject, message, from_email, to_list, fail_silently=True)
        email.send()
        my_form.save()
        my_form = EmailForm()
      except BadHeaderError:
        return HttpResponse('Invalid header found.')
    context = {
      "form"  : my_form
    }

    return render(request, "emails/email_details.html", context)
