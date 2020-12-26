from django.contrib import admin

# Register your models here.
from .models import DOCTOR_DETAILS
admin.site.register(DOCTOR_DETAILS)

from .models import DOCTOR_MONITOR
admin.site.register(DOCTOR_MONITOR)