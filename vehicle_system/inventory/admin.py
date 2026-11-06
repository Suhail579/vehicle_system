from django.contrib import admin

# Register your models here.

from inventory.models import Vehicle , Booking

admin.site.register(Vehicle)
admin.site.register(Booking)
