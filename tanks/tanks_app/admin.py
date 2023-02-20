from django.contrib import admin
from .models import Tank

# Register your models here.
class TankAdmin(admin.ModelAdmin): #to display in columns the details of tanks in the admin page
    list_display = ("tankname", "nationality", "crewmates_num", "turret")


admin.site.register(Tank, TankAdmin)
