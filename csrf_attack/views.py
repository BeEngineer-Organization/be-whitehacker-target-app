from django.shortcuts import render, redirect
from django.views.generic import TemplateView


def teacher_list(request):
    template_name = "csrf_attack/teacher_list.html"

    if request.method == "POST":
        return redirect("attack:teacher")

    else:
        return render(request, template_name)


class TeacherView(TemplateView):
    template_name = "csrf_attack/teacher.html"
