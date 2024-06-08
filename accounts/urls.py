from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("login/", views.MyLoginView.as_view(), name="login"),
    path("sign-up/", views.SignUpView.as_view(), name="sign-up"),
    path("user/update/<int:pk>/", views.UpdateUserView.as_view(), name="update-user"),
    path("password/update", views.UpdatePasswordView.as_view(), name="update-password"),
    path("logout/", views.MyLogoutView.as_view(), name="logout"),
]
