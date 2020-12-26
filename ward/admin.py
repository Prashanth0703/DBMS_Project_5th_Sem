from django.contrib import admin
from doctor.models import DOCTOR_DETAILS

# Register your models here.
from .models import WARD_DETAILS
from .models import DOCTOR_WORKS
from .models import NURSE_WORKS
from .models import WARD_MANAGED_BY

admin.site.register(WARD_DETAILS)
admin.site.register(DOCTOR_WORKS)
admin.site.register(NURSE_WORKS)
admin.site.register(WARD_MANAGED_BY)