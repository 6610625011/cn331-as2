from django.db import models
from django.contrib.auth.models import User


# Create your models here.    
class Course(models.Model):
    subject_id = models.CharField(max_length=10)
    subject_name = models.CharField(max_length=100)
    subject_semester = models.CharField(max_length=10)
    subject_amount = models.IntegerField()
    subject_amount_remaining = models.IntegerField()
    subject_credit = models.IntegerField()
    quota_enabled = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.pk is not None:
            original = Course.objects.get(pk=self.pk)
            if original.subject_amount != self.subject_amount:
                self.subject_amount_remaining = self.subject_amount
        else:
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
