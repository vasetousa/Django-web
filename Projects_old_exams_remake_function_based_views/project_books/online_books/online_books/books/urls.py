from django.urls import path

from online_books.books.views import home_page, profile, profile_edit, \
    profile_delete, profile_create, edit_book, delete_book, book_details_page, add_book

urlpatterns = [
    path('', home_page, name='home page'),

    path('add/', add_book, name='add book'),
    path('edit/<int:pk>/', edit_book, name='edit book'),
    path('delete/<int:pk>/', delete_book, name='delete book'),
    path('details/<int:pk>/', book_details_page, name='book details page'),

    path('profile/', profile, name='profile'),
    path('profile/create/', profile_create, name='profile create'),
    path('profile/edit/', profile_edit, name='profile edit'),
    path('profile/delete/', profile_delete, name='profile delete'),
]
