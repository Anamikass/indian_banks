from django.contrib import admin
from .models import bank_detail

# Register your models here.
admin.site.register(bank_detail)

admin.site.site_header = "Bank Detail Admin"
