from django.contrib import admin
from myapp.models import Student,Course,QuotaRequest

class student_in_admin(admin.ModelAdmin):
    list_display = ['id','name']
    
class subject_in_admin(admin.ModelAdmin):
    list_display = ['subject_id','subject_name','subject_semester','subject_amount']
    
class quotaRequest_in_admin(admin.ModelAdmin):
    list_display = ['user','course','requested_at']

# Register your models here.
admin.site.register(Student,student_in_admin)
admin.site.register(Course,subject_in_admin)
admin.site.register(QuotaRequest,quotaRequest_in_admin)
