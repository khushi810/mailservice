from django.contrib import admin

from .models import Admin
from .models import Email

admin.site.register(Admin)
admin.site.register(Email)
