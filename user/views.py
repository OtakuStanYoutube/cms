from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.messages import error, success
from django.contrib.auth.decorators import login_required
from .authDecorators import unauthenticated_user, is_admin
from .models import User
from .forms import UserForm

# Create your views here.
@login_required(login_url='login-view')
def dashboard_view(request):
    return render(request, 'user/dashboard.html')

@unauthenticated_user
def login_view(request):
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

@login_required(login_url='login-view')
def logout_view(request):
    logout(request)
    success(request, 'Logged out successfully.')
    return redirect('login-view')

@login_required(login_url='login-view')
def users_view(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    
    return render(request, 'user/users.html', context)


@login_required(login_url='login-view')
@is_admin
def create_user_view(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            success(request, 'User created successfully.')
            return redirect('users-view')

    context = {'form': form}
    return render(request, 'user/create_user.html', context)


@login_required(login_url='login-view')
@is_admin
def update_user_view(request,pk):
    user = User.objects.get(pk=pk)
    form = UserForm(instance=user)
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            success(request, 'User updated successfully.')
            return redirect('users-view')
        
    context = {'form': form}
    return render(request, 'user/update_user.html', context)
    