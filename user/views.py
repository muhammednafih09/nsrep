from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from dashboard.views import index
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model



def loginUser(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')

    return render(request, 'registration/login.html', {'page': page})


def logoutUser(request):
    logout(request)
    return redirect('login')


# def registerUser(request):
#     page = 'register'
#     form = CustomUserCreationForm()

#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.save()

#             if user is not None:
#                 login(request, user)
#                 return redirect('dashboard')
#         else:
#             return redirect('login')

#     context = {'form': form, 'page': page}
#     return render(request, 'registration/login.html', context)


@login_required(login_url='login')
def loggedIn(request):
    return index(request)


@login_required(login_url='login')
def addUser(request):
    page = 'add-user'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, "Your account has been created successfully!!")
            return redirect('add-user')

        else:
            messages.success(request, "Enter a valid password!!")

    context = {'form': form, 'page': page}
    return render(request, 'base.html', context)


@login_required(login_url='login')
def viewUser(request):
    page = 'view-user'

    # User = get_user_model()
    # users = User.objects.all()
    users = User.objects.values()


    context = {'page': page, 'users': users}
    return render(request, 'base.html', context)


@login_required(login_url='login')
def profile(request):
    page = 'profile'
    context = {'page': page}
    return render(request,'base.html',context)


@login_required(login_url='login')
def myScans(request):
    page = 'my-scans'
    context = {'page': page}
    return render(request,'base.html',context)


@login_required(login_url='login')
def allScans(request):
    page = 'all-scans'
    context = {'page': page}
    return render(request,'base.html',context)


@login_required(login_url='login')
def reports(request):
    page = 'reports'
    context = {'page': page}
    return render(request,'base.html',context)


@login_required(login_url='login')
def info(request):
    page = 'info'
    context = {'page': page}
    return render(request,'base.html',context)