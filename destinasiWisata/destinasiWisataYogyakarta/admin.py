from django.contrib import admin
from destinasiWisataYogyakarta.models import Destination
# Register your models here.

class DestinationAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'address', 'site',]
    search_fields = ['name', 'description', 'address']
    # list_filter = 
    list_per_page = 5

admin.site.register(Destination, DestinationAdmin)