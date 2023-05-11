from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Review

class SignupForm(UserCreationForm):
    username = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(max_length=150, required=True)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1']

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        fields = ['username', 'password']

class ReviewForm(forms.ModelForm):
    RATINGS = [
        (1, ''),
        (2, ''),
        (3, ''),
        (4, ''),
        (5, ''),
    ]

    rating = forms.ChoiceField(choices=RATINGS, widget=forms.RadioSelect(attrs={'class': 'star'}))
    review_text = forms.CharField(widget=forms.Textarea(attrs={'cols': '30', 'placeholder': 'Describe your experience..'}))

    class Meta:
        model = Review
        fields = ['rating', 'review_text']

issue_choices = [(None, 'Select an issue'),
                 ('Lag', 'Lag'), 
                 ('Bug', 'Bug'), 
                 ('Software Update', 'Software Update'), 
                 ('Multiplayer', 'Multiplayer'), 
                 ('Single Player', 'Single Player'),
                 ('New User', 'New User'),
                 ('General Question', 'General Question'),
                 ('Other', 'Other')]

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'name'}))
    email = forms.EmailField(max_length=150, required=True, widget=forms.TextInput(attrs={'placeholder': 'email'}))
    issue = forms.CharField(required=True, widget=forms.Select(choices=issue_choices))
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={'placeholder': 'message',
                                                           'rows':12,
                                                           'cols':22,
                                                           'style':'resize:none;'}))