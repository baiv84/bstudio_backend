from django.contrib import admin

from .models import Service
from .models import Client
from .models import Master
#from .models import Appointment


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', )

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', )
    
@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    list_display = ('name', )
    raw_id_fields = ('services',)
