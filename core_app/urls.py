from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = "core_app"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),

    # auth
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),

    path("profile/", views.profile, name="profile"),
]
