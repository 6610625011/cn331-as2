from django.shortcuts import render, redirect,get_object_or_404
from myapp.models import Student
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import Course,QuotaRequest


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
    requested_courses = QuotaRequest.objects.filter(user=request.user)

    return render(request, "courses.html", {
        "all_courses": all_courses,
        "requested_courses": requested_courses
    })
    
def request_quota(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    
    if not QuotaRequest.objects.filter(user=request.user, course=course).exists():
        QuotaRequest.objects.create(user=request.user, course=course)
    
    return redirect('/courses')


def logout(request):
    return redirect("/")
