from django.urls import path, re_path
from myapp import views

urlpatterns = [
    path("", views.index),
    path("courses", views.courses),
    path("logout", views.logout),
]
