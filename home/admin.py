from django.contrib import admin
from .models import contactEnquiry

class contactEnquiryAdmin(admin.ModelAdmin):
    list_display = ("name", "email_adress",'Phone','category','Date','message')
admin.site.register(contactEnquiry, contactEnquiryAdmin)
