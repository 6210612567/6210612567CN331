from django.http import response
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User, UserManager
from .models import Courses, Student


class CourseViewTestCase(TestCase):

    def setUp(self):
        user = User.objects.create(username='user1', password=(
            '1234'), email='user1@example.com')
        course = Courses.objects.create(course_code='CN', faculty='Faculty of Engineering', name='MICROPROCESSOR SYSTEMS DESIGN',
                                        courses_id='361', semester=1, year=2021, credit=1, remain=4, seatquota=5)
        course2 = Courses.objects.create(course_code='TU', faculty='Faculty of Engineering', name='x',
                                         courses_id='360', semester=1, year=2021, credit=1, remain=3, seatquota=5)
        course3 = Courses.objects.create(course_code='CU', faculty='Faculty of Engineering', name='y',
                                         courses_id='351', semester=1, year=2021, credit=1, remain=0, seatquota=5)

        student = Student.objects.create(
            student_id=123, student_user=user)
        student.student_courses.add(course)
        student.student_temp.add(course)
        student.save()

    def test_index(self):
        user = User.objects.get(username='user1')
        c = Client()
        c.force_login(user)
        response = c.get(reverse('courses:index'))
        self.assertEqual(response.status_code, 200)

    def test_register(self):
        c = Client()
        user = User.objects.get(username='user1')
        c.force_login(user)
        course = Courses.objects.get(course_code='CN')
        response = c.get(reverse('courses:register',
                         args=(course.courses_id,)))
        self.assertEqual(response.status_code, 302)

    def test_registernotlogin(self):
        c = Client()
        course = Courses.objects.get(course_code='CN')
        response = c.get(reverse('courses:register',
                         args=(course.courses_id,)))
        self.assertEqual(response.status_code, 302)

    def test_remove(self):
        c = Client()
        user = User.objects.get(username='user1')
        c.force_login(user)
        course = Courses.objects.get(course_code='CN')
        response = c.get(reverse('courses:remove',
                         args=(course.courses_id,)))
        self.assertEqual(response.status_code, 302)

    def test_mycourses(self):
        c = Client()
        user = User.objects.get(username='user1')
        c.force_login(user)
        response = c.get(reverse('courses:mycourses'))
        self.assertEqual(response.status_code, 200)

    def test_coursesinfo(self):
        c = Client()
        course = Courses.objects.get(course_code='CN')
        response = c.get(reverse('courses:coursesinfo',
                         args=(course.courses_id,)))
        self.assertEqual(response.status_code, 200)

    def test_confirm(self):
        c = Client()
        user = User.objects.get(username='user1')
        c.force_login(user)
        response = c.get(reverse('courses:confirm'))
        self.assertEqual(response.status_code, 200)

    def test_admin(self):
        c = Client()
        response = c.get(reverse('courses:admin'))
        self.assertEqual(response.status_code, 200)

    def test_admininfo(self):
        c = Client()
        course = Courses.objects.get(course_code='CN')
        response = c.get(reverse('courses:admininfo',
                         args=(course.courses_id,)))
        self.assertEqual(response.status_code, 200)

    def test_c_chance(self):
        c = Client()
        course = Courses.objects.get(course_code='CN')
        response = c.get(reverse('courses:c_chance',
                         args=(course.courses_id,)))
        self.assertEqual(response.status_code, 302)

    def test_c_chanceisfull(self):
        c = Client()
        course = Courses.objects.get(course_code='CU')
        response = c.get(reverse('courses:c_chance',
                         args=(course.courses_id,)))
        self.assertEqual(response.status_code, 302)
