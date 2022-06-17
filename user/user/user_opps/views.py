from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
import user
from user.user_opps.models import SpaceCraft


class HomePage(views.TemplateView):
    model = SpaceCraft
    template_name = 'home_page.html'
    context_object_name = 'current_user'

    def get_context_data(self, **kwargs):
        pass


class RegisterCustomUser(views.FormView):
    template_name = 'register.html'
    context_object_name = 'current_user'
    form_class = UserCreationForm
    success_url = reverse_lazy('index')

    def get(self, *args, **kwargs):  # redirects the user to 'index' if manual change
        if self.request.user.is_authenticated:  # of address field was attempted
            return redirect('index')
        return super(RegisterCustomUser, self).get(*args, **kwargs)


class LoginCustomUser(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('index')
