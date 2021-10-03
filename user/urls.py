from django.urls import path
from .views import home_page, login_page, logout_page

urlpatterns = [
    path('', home_page, name='home-view'),
    path('auth/login/', login_page, name='login-view'),
    path('auth/logout/', logout_page, name='logout-view'),
]