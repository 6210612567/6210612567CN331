from django.db.models.deletion import CASCADE
import courses
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Courses(models.Model):
    course_code = models.CharField(max_length=2, blank=True)
    faculty = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    courses_id = models.IntegerField()
    semester = models.IntegerField()
    year = models.IntegerField()
    credit = models.IntegerField()
    remain = models.IntegerField()
    seatquota = models.IntegerField()

    def isfull(self):
        if self.remain == 0:
            return True
        return False

    def __str__(self):
        return f"{self.course_code} {self.courses_id}"


class Student(models.Model):
    student_id = models.IntegerField()
    student_user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_courses = models.ManyToManyField(
        Courses, blank=True, related_name="student_courses")
    student_temp = models.ManyToManyField(
        Courses, blank=True, related_name="student_temp")

    def __str__(self):
        return f"{self.student_id} {self.student_user}"
