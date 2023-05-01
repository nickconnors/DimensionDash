from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from .forms import LoginForm, SignupForm, ContactForm
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        form = ContactForm(data=request.POST)
        if form.is_valid():
            issue = form.cleaned_data['issue']
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            send_mail(
    		    subject=issue,
    		    message=f"From: {email} ({name})\nMessage:\n{message}",
    		    from_email=settings.EMAIL_HOST_USER,
    		    recipient_list=[settings.EMAIL_HOST_USER])
            messages.success(request, "Message sent")
        else:
            messages.error(request, "Please fill in all fields")
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form' : form})

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
