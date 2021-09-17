from django.urls import path

from . import views

app_name = "courses"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:courses_id>", views.register, name="register"),
    path("mycourses", views.mycourses, name="mycourses"),
    path("coursesinfo/<int:courses_id>", views.coursesinfo, name="coursesinfo"),
    path("confirm", views.confirm, name="confirm"),
    path("remove/<int:courses_id>", views.remove, name="remove"),
    path("admin", views.admin, name="admin"),
    path("admininfo/<int:courses_id>", views.admininfo, name="admininfo"),
    path("c_chance/<int:courses_id>", views.c_chance, name="c_chance"),
]
