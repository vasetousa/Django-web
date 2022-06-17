from django.urls import path

from tools.web_tools.views import show_index

urlpatterns = [
    path('', show_index, name='show index'),
]