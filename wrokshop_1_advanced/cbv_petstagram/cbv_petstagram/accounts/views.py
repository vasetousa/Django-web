# Create your views here.
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


class UserRegisterView():
    pass


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/login_page.html'  # 2 required rows
    success_url = reverse_lazy('dashboard')     # to work properly

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class UserDetailsView:
    pass


class EditProfileView:
    pass


class ChangePasswordView:
    pass
