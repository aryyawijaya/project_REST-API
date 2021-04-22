from django.contrib import admin
from destinasiWisataYogyakarta.models import Destination

class DestinationAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'image_url', 'address', 'site', 'created_at']
    search_fields = ['name', 'description', 'address',]
    list_per_page = 5

admin.site.register(Destination, DestinationAdmin)