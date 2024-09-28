from django.db import models


# Create your models here.
class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=10)
    name = models.CharField(max_length=100)

    def __str__(self):
        # converse obj to str
        return self.id + ", " + str(self.name)
