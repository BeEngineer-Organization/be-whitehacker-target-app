from typing import Any
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .models import CustomUser, TalkRoom, Message
from .forms import MessageForm, CreateTalkRoomForm, UpdateTalkRoomForm


class IndexView(TemplateView):
    template_name = "myapp/index.html"


class TalkRoomListView(TemplateView, LoginRequiredMixin):
    template_name = "myapp/talkroom_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = get_object_or_404(CustomUser, pk=self.request.user.pk)
        context["user"] = user

        talkroom_info = list()
        talkrooms = TalkRoom.objects.filter(users__in=(user,))
        for talkroom in talkrooms:
            latest_message = (
                Message.objects.filter(talkroom=talkroom)
                .order_by("created_at")
                .reverse()
                .first()
            )
            talkroom_info.append((talkroom, latest_message))

        context["talkroom_info"] = talkroom_info
        return context


class TalkRoomView(CreateView, LoginRequiredMixin):
    template_name = "myapp/talkroom.html"
    form_class = MessageForm

    def get_context_data(self, **kwargs):
        # print(str(self.request.headers) + "\n")
        context = super().get_context_data(**kwargs)
        talkroom = get_object_or_404(TalkRoom, pk=self.kwargs["pk"])
        context["user"] = get_object_or_404(CustomUser, pk=self.request.user.pk)
        context["talkroom"] = talkroom
        context["messages"] = Message.objects.filter(talkroom=talkroom).order_by(
            "created_at"
        )
        return context

    def form_valid(self, form):
        form = form.save(commit=False)
        form.talkroom = get_object_or_404(TalkRoom, pk=self.kwargs["pk"])
        form.user = get_object_or_404(CustomUser, pk=self.request.user.pk)
        form.save()
        return redirect("myapp:talkroom", self.kwargs["pk"])

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(TalkRoomView, self).dispatch(*args, **kwargs)


class CreateTalkRoomView(CreateView, LoginRequiredMixin):
    template_name = "myapp/create_talkroom.html"
    form_class = CreateTalkRoomForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["users"] = CustomUser.objects.exclude(pk=self.request.user.pk)
        return context

    def form_valid(self, form):
        object = form.save()
        user_pks = self.request.POST.getlist("users")
        user_pks.append(self.request.user.pk)
        object.users.set(user_pks)
        return redirect("myapp:talkroom-list")


class UpdateTalkRoomView(UpdateView, LoginRequiredMixin):
    template_name = "myapp/update_talkroom.html"
    model = TalkRoom
    form_class = UpdateTalkRoomForm
    success_url = reverse_lazy("myapp:talkroom-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["talkroom"] = get_object_or_404(TalkRoom, pk=self.kwargs["pk"])
        return context


class MypageView(TemplateView, LoginRequiredMixin):
    template_name = "myapp/mypage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = get_object_or_404(CustomUser, pk=self.request.user.pk)
        return context
