from django.urls import path
from destinasiWisataYogyakarta.views import *

urlpatterns = [
    path('destination/', destination_list),
    path('destination/<int:pk>/', destination_detail),
    path('user/', user_list),
    path('user/<int:pk>/', user_detail),
]