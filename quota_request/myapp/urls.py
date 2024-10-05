from django.urls import path, re_path
from myapp import views
from django.contrib.auth import views as auth_views
from .views import request_quota

urlpatterns = [
    path("", views.index),
    path("courses", views.courses),
    path('request_quota/<int:course_id>/', request_quota, name='request_quota'),    
    path('cancel_quota_request/<int:course_id>/', views.cancel_quota_request, name='cancel_quota_request'),
    path("mycourse", views.mycourse),       
    path("logout", auth_views.LogoutView.as_view(), name="logout"), 
]
