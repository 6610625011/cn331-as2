from django.shortcuts import render, redirect
from myapp.models import Student
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login


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
    return render(request, "courses.html")


def logout(request):
    return redirect("/")
