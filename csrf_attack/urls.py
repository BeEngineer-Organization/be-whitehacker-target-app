from django.urls import path

from . import views

app_name = "attack"

urlpatterns = [
    path("teacher-list/", views.teacher_list, name="teacher-list"),
    path("teacher-list/1/", views.TeacherView.as_view(), name="teacher"),
]
