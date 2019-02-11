from django.contrib import admin

# Register your models here.

from .models import Admin
from .models import Email
#from .models import CSV

admin.site.register(Admin)
admin.site.register(Email)
#admin.site.register(CSV)
