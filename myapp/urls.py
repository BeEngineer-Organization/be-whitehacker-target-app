from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = "myapp"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("talkroom-list/", views.TalkRoomListView.as_view(), name="talkroom-list"),
    path("talkroom/<int:pk>/", views.TalkRoomView.as_view(), name="talkroom"),
    path(
        "create-talkroom/", views.CreateTalkRoomView.as_view(), name="create-talkroom"
    ),
    path(
        "talkroom/update/<int:pk>/",
        views.UpdateTalkRoomView.as_view(),
        name="update-talkroom",
    ),
    path("mypage/", views.MypageView.as_view(), name="mypage"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
