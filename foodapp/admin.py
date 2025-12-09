from django.contrib import admin
# in admin.py
from .models import Customer, Restaurant, MenuItem
admin.site.register(Customer)
admin.site.register(Restaurant)
admin.site.register(MenuItem)

# Register your models here.
