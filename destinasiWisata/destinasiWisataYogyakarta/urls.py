from django.urls import path
from destinasiWisataYogyakarta.views import *

urlpatterns = [
    path('destination/', DestinationList.as_view()),
    path('destination/<int:pk>/', DestinationDetail.as_view()),
    path('user/', UserList.as_view()),
    path('user/<int:pk>/', UserDetail.as_view()),
]