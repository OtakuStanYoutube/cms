from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home-view')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

def is_admin(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_superuser or request.user.role == 'Admin':
            return view_func(request, *args, **kwargs)
        else:
             return redirect('home-view')
    return wrapper_func