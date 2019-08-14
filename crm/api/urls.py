from django.urls import path, include
from .views import *


urlpatterns = [
    path('users/', UsersAPI.as_view(), name='users'),
    # path('login/', login, name='login'),
]