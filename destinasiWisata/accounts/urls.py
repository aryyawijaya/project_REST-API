from django.urls import path
from accounts.views import *

urlpatterns = [
    path('user/', UserList.as_view()),
    path('user/<int:pk>/', UserDetail.as_view()),
    path('user/register/', RegisterAPI.as_view()),
    path('user/login/', LoginAPI.as_view()),
    path('user/logout/', LogoutAPI.as_view()),
]