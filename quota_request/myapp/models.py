from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=10)
    name = models.CharField(max_length=100)

    def __str__(self):
        # converse obj to str
        return self.id + ", " + str(self.name)

class Course(models.Model):
    subject_id = models.CharField(max_length=10)
    subject_name = models.CharField(max_length=100)
    subject_semester = models.CharField(max_length=10)
    subject_amount = models.IntegerField()
    subject_amount_remaining = models.IntegerField()
    quota_enabled = models.BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        if self.pk is None: 
            self.subject_amount_remaining = self.subject_amount
        super().save(*args, **kwargs)    

    def __str__(self):
        return self.subject_id
    
class QuotaRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    requested_at = models.DateTimeField(auto_now_add=True)    

    def __str__(self):
        return f"{self.user.username} - {self.course.subject_id}"
