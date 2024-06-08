from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    image = models.ImageField(upload_to="images/user/", blank=True)


class TalkRoom(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to="images/talkroom/", blank=True)
    users = models.ManyToManyField(CustomUser)

    def __str__(self):
        return self.name


class Message(models.Model):
    content = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    talkroom = models.ForeignKey(TalkRoom, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
