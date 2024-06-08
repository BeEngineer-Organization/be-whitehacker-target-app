from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect

from myapp.models import CustomUser
from .forms import LoginForm, SignUpForm, UpdateUserForm


class MyLoginView(LoginView):
    template_name = "accounts/login.html"
    form_class = LoginForm

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        if self.redirect_authenticated_user and self.request.user.is_authenticated:
            redirect_to = self.get_success_url()
            return HttpResponseRedirect(redirect_to)
        return super(LoginView, self).dispatch(request, *args, **kwargs)


class SignUpView(CreateView):
    template_name = "accounts/signup.html"
    form_class = SignUpForm
    success_url = reverse_lazy("myapp:index")


class UpdateUserView(UpdateView, LoginRequiredMixin):
    template_name = "accounts/update_user.html"
    model = CustomUser
    form_class = UpdateUserForm
    success_url = reverse_lazy("myapp:mypage")

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(UpdateUserView, self).dispatch(*args, **kwargs)


class UpdatePasswordView(PasswordChangeView, LoginRequiredMixin):
    template_name = "accounts/update_password.html"
    success_url = reverse_lazy("myapp:mypage")


class MyLogoutView(LogoutView, LoginRequiredMixin):
    template_name = "account/login.html"

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(LogoutView, self).dispatch(request, *args, **kwargs)
