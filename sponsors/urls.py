from django.urls import path
from .views import sponsors_view, create_sponsor_view

urlpatterns = [
    path('', sponsors_view, name='sponsors-view'),
    path('/create-sponsors', create_sponsor_view, name='create-sponsors-view'),
]