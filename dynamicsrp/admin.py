"""Admin models"""

# Django
from django.contrib import admin  # noqa: F401
from .models import *

# Register your models here.
admin.site.register(Ship)
admin.site.register(Reimbursement)
admin.site.register(Payout)
admin.site.register(Setting)