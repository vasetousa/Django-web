from django.urls import path

from books.online_books.views import add_book_page, edit_book_page, \
    delete_book_page, profile_page, edit_profile_page, delete_profile_page, create_profile_page, home_page, \
    book_details_page

urlpatterns = [
    path('', home_page, name='home page'),

    path('add/', add_book_page, name='add book page'),
    path('edit/<int:pk>/', edit_book_page, name='edit book page'),
    path('delete/<int:pk>/', delete_book_page, name='delete book page'),
    path('details/<int:pk>/', book_details_page, name='book details page'),

    path('profile/', profile_page, name='profile page'),
    path('profile/edit/', edit_profile_page, name='edit profile page'),
    path('profile/delete/', delete_profile_page, name='delete profile page'),
    path('profile/create/', create_profile_page, name='create profile page'),
]
