from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.messages import error, success

# Create your views here.
def home_page(request):
    return render(request, 'user/dashboard.html')

def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, email=email, password=password)
        if user is not None:
            login(request, user)
            success(request, 'Logged in successfully.')
            return redirect('home-page')
        else:
            error(request, 'Invalid username or password.')
            return render(request, 'user/login.html')
    return render(request, 'user/login.html')