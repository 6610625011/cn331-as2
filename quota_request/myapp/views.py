from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import Course,QuotaRequest
from django.contrib.auth import authenticate, login



# Create your views here.
def index(request):
    return redirect('login')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username") 
        password = request.POST.get("password") 
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/courses')  
        else:
            error_message = "Invalid username or password."
            return render(request, "index.html", {"error": error_message})
    return render(request, "courses.html")

@login_required(login_url='/users/login/')
def courses(request):
    all_courses = Course.objects.all()
    requested_courses = QuotaRequest.objects.filter(user=request.user).select_related('course')
    
    requested_course_ids = requested_courses.values_list('course_id', flat=True)

    available_courses = Course.objects.exclude(id__in=requested_course_ids) 
    
    selected_semester = request.GET.get('semester', None)

    if selected_semester:
        all_courses = all_courses.filter(subject_semester=selected_semester)

    semesters = Course.objects.values_list('subject_semester', flat=True).distinct()

    return render(request, "courses.html", {
        "all_courses": all_courses,
        "requested_course_ids": requested_course_ids, 
        "available_courses": available_courses,
        "semesters": semesters,
        "selected_semester": selected_semester,
    })

    
def request_quota(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    
    if not QuotaRequest.objects.filter(user=request.user, course=course).exists():
        if course.subject_amount_remaining > 0:
            QuotaRequest.objects.create(user=request.user, course=course)

            course.subject_amount_remaining -= 1
            course.save()

            messages.success(request, 'ขอโควต้าสำเร็จ')
        # else:
        #     messages.error(request, 'ขอโควต้าไม่สำเร็จ: วิชานี้เต็มแล้ว')
    # else:
    #     messages.error(request, 'คุณได้ขอโควต้าในวิชานี้แล้ว')
    return redirect('/courses')


def cancel_quota_request(request, course_id):
    course = get_object_or_404(Course, id=course_id)    
    quota_request = get_object_or_404(QuotaRequest, user=request.user, course_id=course_id)
    
    quota_request.delete()
    
    course.subject_amount_remaining += 1
    course.save()    
    
    messages.success(request, "ยกเลิกการขอโควต้าแล้ว")
    return redirect('/mycourse')

@login_required(login_url='/users/login/')
def mycourse(request):
    requested_courses = QuotaRequest.objects.filter(user=request.user)
    context = {
        'requested_courses': requested_courses,
    }
    return render(request, 'mycourse.html', context)


def logout(request):
    return redirect("login")
