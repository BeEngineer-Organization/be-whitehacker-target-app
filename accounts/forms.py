from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    UserChangeForm,
)

from myapp.models import CustomUser


class LoginForm(AuthenticationForm):
    pass


class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["username", "image", "password1", "password2"]


class UpdateUserForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ["username", "image"]
