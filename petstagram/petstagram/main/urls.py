from django.urls import path

from petstagram.main.views.generic import  HomeView, DashboardView
from petstagram.main.views.pet_photos import edit_pet_photo, like_pet_photo, \
    AddPetPhotoView, PetPhotoDetailsView
from petstagram.main.views.pets import AddPetView, EditPetView, DeletePetView
from petstagram.main.views.profiles import create_profile, edit_profile, delete_profile, ProfileDetailsView

'''
Home Page: http://127.0.0.1:8000/ 
Dashboard Page: http://127.0.0.1:8000/dashboard/ 
Profile Page: http://127.0.0.1:8000/profile/ 
Photo Details Page: http://127.0.0.1:8000/photo/details/photo_id/
'''

urlpatterns = (
    path('', HomeView.as_view(), name='index'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    path('profile/<int:pk>/', ProfileDetailsView.as_view(), name='profile details'),
    path('profile/create/', create_profile, name='create profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),

    path('pet/add/', AddPetView.as_view(), name='add pet'),
    path('pet/edit/<int:pk>/', EditPetView.as_view(), name='edit pet'),
    path('pet/delete/<int:pk>/', DeletePetView.as_view(), name='delete pet'),

    path('photo/add/', AddPetPhotoView.as_view(), name='add pet photo'),
    path('photo/edit/<int:pk>/', edit_pet_photo, name='edit pet photo'),
    path('photo/details/<int:pk>/', PetPhotoDetailsView.as_view(), name='pet photo details'),
    path('photo/like/<int:pk>/', like_pet_photo, name='like pet photo'),

)
