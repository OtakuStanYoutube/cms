from django.urls import path
from .views import home_page, login_page

urlpatterns = [
    path('', home_page, name='home-view'),
    path('login/', login_page, name='login-view'),
]