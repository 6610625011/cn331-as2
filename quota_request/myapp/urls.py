from django.urls import path, re_path
from myapp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.index),
    path("courses", views.courses),
    path("logout", auth_views.LogoutView.as_view(), name="logout"),  # Use Django's built-in LogoutView
]
