from django.contrib import admin

# Register your models here.
from .models import PATIENT_DETAILS
admin.site.register(PATIENT_DETAILS)

from patient.models import DEPENDENT
admin.site.register(DEPENDENT)

from .models import ADMITTED_TO
admin.site.register(ADMITTED_TO)

# from .models import HAS_DEPENDENT
# admin.site.register(HAS_DEPENDENT)

from .models import DECISION_MAKING
admin.site.register(DECISION_MAKING)

from .models import PAYMENT
admin.site.register(PAYMENT)

from .models import HOME_QUARANTINE_MONITOR
admin.site.register(HOME_QUARANTINE_MONITOR)

from .models import HAS_BANK
admin.site.register(HAS_BANK)

from .models import HAS_INSURANCE
admin.site.register(HAS_INSURANCE)

from .models import DEP_MONITOR
admin.site.register(DEP_MONITOR)