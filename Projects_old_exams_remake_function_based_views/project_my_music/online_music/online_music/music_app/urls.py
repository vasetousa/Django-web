from django.urls import path

from online_music.music_app.views import home_page, album_add, album_edit, album_delete, profile_create, album_details, \
    profile_details, profile_delete, profile_delete_final, album_delete_final

urlpatterns = [
    path('', home_page, name='home page'),

    path('album/add/', album_add, name='album add'),
    path('album/details/<int:pk>/', album_details, name='album details'),
    path('album/edit/<int:pk>/', album_edit, name='album edit'),
    path('album/delete/<int:pk>/', album_delete, name='album delete'),
    path('album/delete/clear/<int:pk>/', album_delete_final, name='album delete final'),

    path('profile/create/', profile_create, name='profile create'),
    path('profile/details/', profile_details, name='profile details'),
    path('profile/delete/', profile_delete, name='profile delete'),
    path('profile/delete/clear/', profile_delete_final, name='profile delete final'),
]