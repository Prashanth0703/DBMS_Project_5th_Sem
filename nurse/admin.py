from django.contrib import admin

# Register your models here.
from .models import NURSE_DETAILS
admin.site.register(NURSE_DETAILS)

from .models import NURSE_MONITOR
admin.site.register(NURSE_MONITOR)
