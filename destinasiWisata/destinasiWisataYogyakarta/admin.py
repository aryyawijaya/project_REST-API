from django.contrib import admin
from destinasiWisataYogyakarta.models import Destination
# Register your models here.

class DestinationAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'image_url', 'address', 'site', 'created_at']
    search_fields = ['name', 'description', 'address',]
    # list_filter = 
    list_per_page = 5

# class UserAdmin(admin.ModelAdmin):
#     list_display = ['username', 'email', 'password',]
#     search_fields = ['username', 'email',]
#     list_per_page = 5

admin.site.register(Destination, DestinationAdmin)
# admin.site.register(User, UserAdmin)