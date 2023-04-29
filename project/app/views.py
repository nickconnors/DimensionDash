from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from .forms import LoginForm, SignupForm

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def reviewus(request):
    if request.user.is_authenticated:
        return render(request, 'reviewus.html')
    else:
        return redirect('index')

def registerUser(request):
    if request.method == "POST":
        form = SignupForm(data=request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('index')
    else:
        form = SignupForm()
    return render(request, 'register.html', {'form' : form})

def loginUser(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                    login(request, user)
                    return redirect('index')
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form' : form})

def logoutUser(request):
    logout(request)
    return redirect('index')
