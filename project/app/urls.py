from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("contact/", views.contact, name="contact"),
    path("reviewus/", views.reviewus, name="reviewus"),
    path("reviews/", views.reviews, name="reviews"),
    path("login/", views.loginUser, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("register/", views.registerUser, name="register"),
    path("about/", views.about, name="about"),
    path("download/", views.download, name="download"),
    path("submit_score/", views.submit_score, name="submit_score")
]