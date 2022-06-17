from django.urls import path

from online_recipes.recipes.views import index, create, edit, delete, details

urlpatterns = [
    path('', index, name='index'),

    path('create/', create, name='create'),
    path('edit/<int:pk>/', edit, name='edit recipe'),
    path('delete/<int:pk>/', delete, name='delete recipe'),
    path('details/<int:pk>/', details, name='details recipe'),
]
