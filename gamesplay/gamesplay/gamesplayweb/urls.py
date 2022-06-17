from django.urls import path

from gamesplay.gamesplayweb.views import index, profile_create, profile_edit, profile_delete, profile_details, \
    dashboard, game_create, game_edit, game_delete, profile_delete_confirm, game_details

urlpatterns = [
    path('', index, name='index'),

    path('profile/create/', profile_create, name='profile create'),
    path('profile/edit/', profile_edit, name='profile edit'),
    path('profile/delete/', profile_delete, name='profile delete'),
    path('profile/delete/confirm/', profile_delete_confirm, name='profile delete confirm'),
    path('profile/details/', profile_details, name='profile details'),


    path('dashboard/', dashboard, name='dashboard'),


    path('game/create/', game_create, name='game_create'),
    path('game/details/<int:pk>/', game_details, name='game_details'),
    path('game/edit/<int:pk>/', game_edit, name='game_edit'),
    path('game/delete/<int:pk>/', game_delete, name='game_delete'),
]
