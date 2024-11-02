from django.urls import path, re_path
from myapp import views
from django.contrib.auth import views as auth_views
from .views import request_quota,login_view,logout

urlpatterns = [
    path("", views.index,name='index'),
    path('login/', login_view, name='login'),    
    path("courses", views.courses, name='courses'),
    path('request_quota/<int:course_id>/', request_quota, name='request_quota'),    
    path('cancel_quota_request/<int:course_id>/', views.cancel_quota_request, name='cancel_quota_request'),
    path("mycourse", views.mycourse, name='mycourse'),       
    path('logout/', logout, name='logout'),
 
]
