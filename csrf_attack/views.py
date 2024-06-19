from django.shortcuts import render


def teacher_list(request):
    template_name = "csrf_attack/teacher_list.html"
    # ここに処理を記述
    return render(request, template_name)