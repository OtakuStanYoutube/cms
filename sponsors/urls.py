from django.urls import path
from .views import sponsors_view

urlpatterns = [
    path('', sponsors_view, name='sponsors-view'),
]