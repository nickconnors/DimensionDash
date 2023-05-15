from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from .forms import LoginForm, SignupForm, ContactForm, ReviewForm
from django.core.mail import send_mail
from django.conf import settings
from .models import Review, UserScore
from django.views.decorators.csrf import csrf_exempt


def index(request):
    scores = UserScore.objects.all().order_by('-highscore')
    return render(request, 'index.html', context={'user_scores': scores})

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
        if request.method == "POST":
            form = ReviewForm(data=request.POST)
            if form.is_valid():
                rating = int(form.cleaned_data['rating'])
                review_text = form.cleaned_data['review_text']
                user = request.user

                try:
                    review = Review.objects.get(user=user)
                    review.rating = rating
                    review.review_text = review_text
                    review.save()
                except Review.DoesNotExist:
                    review = Review(user=user, rating=rating, review_text=review_text)
                    review.save()

                return JsonResponse({'rating': rating, 'review_text': review_text})
            else:
                return JsonResponse({'error': 'Form is not valid'})

        else:
            try:
                review = Review.objects.get(user=request.user)
                context = {'form': ReviewForm(), 'review_exists': True, 'rating': review.rating, 'review_text': review.review_text}
            except Review.DoesNotExist:
                context = {'form': ReviewForm(), 'review_exists': False}

            return render(request, 'reviewus.html', context)

    else:
        return redirect('login')

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

def reviews(request):
    reviews = Review.objects.all()
    review_exists = False
    if request.user.is_authenticated:
        try:
            review = reviews.get(user=request.user)
            review_exists = True
        except Review.DoesNotExist:
            pass

    return render(request, 'reviews.html', context={'reviews': reviews, 'review_exists': review_exists})

def download(request):
    if request.user.is_authenticated:
        return render(request, 'download.html')
    else:
        return redirect('login')
    
@csrf_exempt
def submit_score(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            score = int(request.POST.get("score", 0))

            user = request.user

            try:
                user_score = UserScore.objects.get(user=user)
                if score > user_score.highscore:
                    user_score.highscore = score
                    user_score.save()
            except UserScore.DoesNotExist:
                user_score = UserScore(user=user, highscore=score)
                user_score.save()
                    
            return redirect('index')
        else:
            return render(request, 'submit_score.html')
    else:
        return redirect('login')