from django.urls import path
from .views import home, login

urlpatterns = [
    path('', home, name='home-view'),
    path('login/', login, name='login-view'),
]