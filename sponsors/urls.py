from django.urls import path
from .views import sponsors_view, create_sponsor_view, update_sponsor_view

urlpatterns = [
    path('', sponsors_view, name='sponsors-view'),
    path('create-sponsor/', create_sponsor_view, name='create-sponsor-view'),
    path('update-sponsor/<str:pk>', update_sponsor_view, name='update-sponsor-view'),
]