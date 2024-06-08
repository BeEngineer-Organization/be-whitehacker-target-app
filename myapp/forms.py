from django import forms

from .models import CustomUser, Message, TalkRoom


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["content"]


class CreateTalkRoomForm(forms.ModelForm):
    class Meta:
        model = TalkRoom
        fields = ["name", "image"]


class UpdateTalkRoomForm(forms.ModelForm):
    class Meta:
        model = TalkRoom
        fields = ["name", "image", "users"]
