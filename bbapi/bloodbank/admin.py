from django.contrib import admin

# Register your models here.

from .models import *


admin.site.register(Donor)
admin.site.register(Patient)
admin.site.register(County)
admin.site.register(SubCounty)