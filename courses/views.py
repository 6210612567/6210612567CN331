import courses
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

# Create your views here.

from .models import Courses, Student


def index(request):
    student = Student.objects.get(student_user=request.user)
    temp = []
    allcourses = []

    for course in Courses.objects.all():
        if (course not in student.student_courses.all()) and (course not in student.student_temp.all()):
            allcourses.append((course, course.isfull()))
        if (course in student.student_temp.all()) or (course in student.student_courses.all()):
            temp.append(course)

    return render(request, "courses/index.html", {
        "allcourses": allcourses,
        "temp": temp,
    })


def register(request, courses_id):
    if not request.user.is_authenticated:
        messages.warning(request, "Please Login")
        return HttpResponseRedirect(reverse("users:login")+f"?next={request.path}")

    course = Courses.objects.get(courses_id=courses_id)
    student = Student.objects.get(student_user=request.user)
    student.student_temp.add(course)
    student.save()
    course.remain -= 1
    course.save()

    return HttpResponseRedirect(reverse("courses:index"))


def remove(request, courses_id):
    course = Courses.objects.get(courses_id=courses_id)
    student = Student.objects.get(student_user=request.user)
    student.student_temp.remove(course)
    student.student_courses.remove(course)
    student.save()
    course.remain += 1
    course.save()

    return HttpResponseRedirect(reverse("courses:index"))


def mycourses(request):
    student = Student.objects.get(student_user=request.user)

    return render(request, "courses/mycourses.html", {
        "student_courses": student.student_courses.all()
    })


def coursesinfo(request, courses_id):
    courses_info = Courses.objects.get(courses_id=courses_id)

    return render(request, "courses/coursesinfo.html", {
        "courses_info": courses_info,
        "check": courses_info.isfull(),
    })


def confirm(request):
    student = Student.objects.get(student_user=request.user)

    for course in student.student_temp.all():
        student.student_courses.add(course)
        student.student_temp.remove(course)

    student.save()

    return render(request, "courses/confirm.html", {
        "c_courses": student.student_courses.all()
    })


def admin(request):
    return render(request, "courses/admin.html", {
        "allcourses": Courses.objects.all()
    })


def admininfo(request, courses_id):
    courses_info = Courses.objects.get(courses_id=courses_id)
    student = Student.objects.all()
    student_name = []
    student_last = []

    for i in student:
        for j in i.student_courses.all():
            if j == courses_info:
                student_name.append(i.student_user)
                student_last.append(i.student_user.last_name)

    return render(request, "courses/admin_info.html", {
        "courses_info": courses_info,
        "student_name": student_name,
        "student_last": student_last,
        "check": courses_info.isfull(),
    })


def c_chance(request, courses_id):
    courses = Courses.objects.get(courses_id=courses_id)

    if(courses.isfull()):
        courses.remain = courses.seatquota
    else:
        courses.remain = 0

    courses.save()

    return HttpResponseRedirect(reverse("courses:index"))
