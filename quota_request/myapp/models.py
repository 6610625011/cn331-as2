from django.db import models


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
    # is_quota_open = models.BooleanField(default=True)

    def __str__(self):
        return self.subject_id
    

