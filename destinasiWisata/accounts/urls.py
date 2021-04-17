from django.urls import path
from accounts.views import *
from knox.views import LogoutView, LogoutAllView

urlpatterns = [
    path('user/', UserList.as_view()),
    path('user/<int:pk>/', UserDetail.as_view()),
    path('user/register/', RegisterAPI.as_view()),
    path('user/login/', LoginAPI.as_view()),
    path('user/logout/', LogoutView.as_view()),
    path('user/logoutall/', LogoutAllView.as_view()),
]