from django.contrib import admin
from myapp.models import Student
from myapp.models import Course

# Register your models here.
admin.site.register(Student)
admin.site.register(Course)
