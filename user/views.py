from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.messages import error, success
from django.contrib.auth.decorators import login_required
from .authDecorators import unauthenticated_user

# Create your views here.
@login_required(login_url='login-view')
def home_page(request):
    return render(request, 'user/dashboard.html')

@unauthenticated_user
def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            success(request, 'Logged in successfully.')
            return redirect('home-view')
        else:
            error(request, 'Invalid username or password.')
            return render(request, 'auth/login.html')
    
    return render(request, 'auth/login.html')

def logout_page(request):
    logout(request)
    success(request, 'Logged out successfully.')
    return redirect('login-view')