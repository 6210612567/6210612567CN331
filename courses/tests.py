from django.http import response
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Courses, Student

# Create your tests here.


class CourseViewTestCase(TestCase):

    def setUp(self):
        user = User.objects.create(username='user1', password=(
            '1234'), email='user1@example.com')
        course = Courses.objects.create(course_code='CN', faculty='Faculty of Engineering', name='MICROPROCESSOR SYSTEMS DESIGN',
                                        courses_id='361', semester=1, year=2021, credit=1, remain=4, seatquota=5)

    def test_isfull(self):
        course = Courses.objects.create(course_code='CN', faculty='Faculty of Engineering', name='MICROPROCESSOR SYSTEMS DESIGN',
                                        courses_id='361', semester=1, year=2021, credit=1, remain=0, seatquota=5)

        self.assertTrue(course.isfull())

    def test_isnotfull(self):
        course = Courses.objects.create(course_code='CN', faculty='Faculty of Engineering', name='MICROPROCESSOR SYSTEMS DESIGN',
                                        courses_id='361', semester=1, year=2021, credit=1, remain=4, seatquota=5)

        self.assertFalse(course.isfull())

    def test_str_course(self):
        course = Courses.objects.create(course_code='CN', faculty='Faculty of Engineering', name='MICROPROCESSOR SYSTEMS DESIGN',
                                        courses_id='361', semester=1, year=2021, credit=1, remain=4, seatquota=5)
        self.assertEqual(str(course), course.course_code+' '+course.courses_id)

    def test_str_student(self):
        user2 = User.objects.create(username='user2', password=(
            ''), email='user2@example.com')
        course = Courses.objects.get(course_code='CN')
        student = Student.objects.create(
            student_id='126', student_user=user2)
        student.student_courses.add(course)
        student.student_temp.add(course)
        student.save()
        self.assertEqual(str(student), student.student_id +
                         ' '+str(student.student_user))
