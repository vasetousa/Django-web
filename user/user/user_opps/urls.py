from django.contrib.auth.views import LogoutView
from django.urls import path

from user.user_opps.views import RegisterCustomUser, HomePage, LoginCustomUser

urlpatterns = [
    path('', HomePage.as_view(), name='index'),
    path('register/', RegisterCustomUser.as_view(), name='register'),
    path('login/', LoginCustomUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),

]