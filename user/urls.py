from django.urls import path
from .views import dashboard_view, login_view, logout_view, users_view

urlpatterns = [
    path('', dashboard_view, name='home-view'),
    path('users/', users_view, name='users-view'),
    path('auth/login/', login_view, name='login-view'),
    path('auth/logout/', logout_view, name='logout-view'),
]