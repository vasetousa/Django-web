from django.shortcuts import render, redirect
from cbv_petstagram.petstagram.views.helpers import get_profile
from cbv_petstagram.petstagram.models import PetPhoto


def show_pet_photo_details(request, pk):
    # pet_photo = PetPhoto.objects.get(id=pk) same as below
    pet_photo = PetPhoto.objects.get(pk=pk)

    context = {
        'pet_photo': pet_photo,
    }

    return render(request, 'main/photo_details.html', context)


def like_pet_photo(request, pk):
    pet_photo = PetPhoto.objects.get(pk=pk)
    pet_photo.likes += 1
    pet_photo.save()
    return redirect('pet photo details', pk)


def add_pet_photo(request):
    return render(request, 'main/photo_create.html')


def edit_pet_photo(request):
    return render(request, 'main/photo_edit.html')
