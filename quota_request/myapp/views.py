from django.shortcuts import render, redirect
from myapp.models import Student
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from .models import Course


# Create your views here.
def index(request):
    if request.method == "POST":
        id = request.POST["id"]
    #    form = AuthenticationForm(data=request.POST)
    #    if form.is_valid():
    #        user = form.get_user()
    #        login(request, user)
    #        return redirect("courses.html")
    # else:
    #    form = AuthenticationForm()
    # return render(
    #    request,
    #    "index.html",
    #    {
    #        "form": form,
    #    },
    # )
    # student_id = Student.objects.get(id)
    # student_password = Student.objects.get(password)

    #
    # if request.method == "POST":
    return render(request, "index.html")


def courses(request):
    all_courses = Course.objects.all()
    return render(request,"courses.html",{"all_courses":all_courses})
    # course = Course.objects.get(subject_id="CN331")

    # context = {
    #     'subject_id': course.subject_id,
    #     'subject_name': course.subject_name,
    #     'subject_semester': course.subject_semester,
    #     'subject_amount': course.subject_amount,
    #     # 'subject_status': "Open" if course.is_quota_open else "Closed"  # Display open/closed status
    # }

    # return render(request, "courses.html", context)



def logout(request):
    return redirect("/")
