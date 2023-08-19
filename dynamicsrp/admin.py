"""Admin models"""

# Django
from django.contrib import admin

from .models import *

class PayoutAdmin(admin.ModelAdmin):
    search_fields = ['ship__name']

class ReimbursementAdmin(admin.ModelAdmin):
    search_fields = ['name']

class ShipAdmin(admin.ModelAdmin):
    search_fields = ['name']

class SettingAdmin(admin.ModelAdmin):
    search_fields = ['name']

admin.site.register(Ship, ShipAdmin)
admin.site.register(Reimbursement, ReimbursementAdmin)
admin.site.register(Payout, PayoutAdmin)
admin.site.register(Setting, SettingAdmin)
admin.site.register(SRPRequest)
