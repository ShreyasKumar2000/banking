

# Register your models here.


# banking_app/admin.py
from django.contrib import admin
from .models import Customer,District,Branch

admin.site.register(Customer)
admin.site.register(District)
admin.site.register(Branch)