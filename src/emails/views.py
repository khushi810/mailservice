from django.shortcuts import render
from .models import Email
from .forms import EmailForm

# Create your views here.

def email_view(request):
      my_form = EmailForm(request.POST or None)
      if my_form.is_valid():
        my_form.save()
      # if request.method == 'POST':
      #   my_form = EmailForm(request.POST)
      #   print(my_form.cleaned_data)
      # else:
      #   print(my_form.errors)

      context = {
          "form"  : my_form
      }

      return render(request, "emails/email_details.html", context)
