from django.urls import path
from django.views.generic import TemplateView

from user.user_pass.views import UserRegistrationView, UserLoginView, UserLogoutView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),

]