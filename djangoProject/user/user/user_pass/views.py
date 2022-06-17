from django.contrib.auth import forms as auth_forms, get_user_model, login
from django.contrib.auth.views import LoginView, LogoutView

from django.contrib.auth import models as auth_models
# Create your views here.
from django.urls import reverse_lazy
from django.views import generic as views

from user.user_pass.models import Employee

'''
Variant 1, using Django's build in form UserCreationForm
                    vvvvvvvvvvvvvvv
'''
# class UserRegistrationView(views.CreateView):
#     form_class = auth_forms.UserCreationForm
#     template_name = 'register.html'
#     success_url = reverse_lazy('index')
#


'''
Variant 2, using our CUSTOM form UserRegisterForm
                    vvvvvvvvvvvvvvv
'''
UserModel = get_user_model()


class UserRegistrationForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email',)

    def clean_email(self):
        return self.cleaned_data['email']

    def save(self, commit=True):
        return super().save(commit=commit)


class UserRegistrationView(views.CreateView):
    form_class = UserRegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy('index')

    '''
    autologin for the created user
    '''

    def form_valid(self, *args, **kwargs):
        result = super().form_valid(*args, **kwargs)
        # user -> self.object
        # request -> self.request
        login(self.request, self.object)
        return result


class UserLoginView(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('index')


class UserLogoutView(LogoutView):
    template_name = 'logout.html'

    def get_next_page(self):
        return reverse_lazy('index')


