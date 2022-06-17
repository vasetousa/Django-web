from django.urls import path

from cbv_petstagram.petstagram.views.generic import HomeView, error_401, DashboardView
from cbv_petstagram.petstagram.views.pet_photos import add_pet_photo, edit_pet_photo, show_pet_photo_details, \
    like_pet_photo
from cbv_petstagram.petstagram.views.pets import CreatePetView, EditPetView, DeletePetView
from cbv_petstagram.petstagram.views.profiles import show_profile, create_profile, edit_profile, delete_profile

'''
Home Page: http://127.0.0.1:8000/ 
Dashboard Page: http://127.0.0.1:8000/dashboard/ 
Profile Page: http://127.0.0.1:8000/profile/ 
Photo Details Page: http://127.0.0.1:8000/photo/details/photo_id/
'''

urlpatterns = (
    path('', HomeView.as_view(), name='index'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('401/', error_401, name='error 401'),


    path('profile/', show_profile, name='profile details'),
    path('profile/create/', create_profile, name='create profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),

    path('pet/add/', CreatePetView.as_view(), name='add pet'),
    path('pet/edit/<int:pk>/', EditPetView.as_view(), name='edit pet'),
    path('pet/delete/<int:pk>/', DeletePetView.as_view(), name='delete pet'),

    path('photo/add/', add_pet_photo, name='add pet photo'),
    path('photo/edit/<int:pk>/', edit_pet_photo, name='edit pet photo'),
    path('photo/details/<int:pk>/', show_pet_photo_details, name='pet photo details'),
    path('photo/like/<int:pk>/', like_pet_photo, name='like pet photo'),

)
