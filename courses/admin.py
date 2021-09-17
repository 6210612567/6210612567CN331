from django.contrib import admin

# Register your models here.

from .models import *


class CoursesAdmin(admin.ModelAdmin):
    list_display = ("course_code", "courses_id", "name", "faculty", "semester",
                    "year", "seatquota", "remain", "credit")


class StudentAdmin(admin.ModelAdmin):
    filter_horizontal = ("student_courses",)


admin.site.register(Courses, CoursesAdmin)
admin.site.register(Student, StudentAdmin)
