
from django.shortcuts import render, redirect

from cbv_petstagram.petstagram.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
from cbv_petstagram.petstagram.models import Profile, PetPhoto, Pet
from cbv_petstagram.petstagram.views.helpers import get_profile


def show_profile(request):
    profile = get_profile()
    pets = list(Pet.objects.filter(user_profile=profile))
    total_likes_count = sum(pp.likes for pp in PetPhoto.objects
                            .filter(tagged_pets__user_profile=profile) \
                            .distinct()
                            )

    total_pets_photo_count = len(PetPhoto.objects
                                 .filter(tagged_pets__user_profile=profile) \
                                 .distinct()
                                 )

    context = {
        'profile': profile,
        'total_likes_count': total_likes_count,
        'total_pets_photo_count': total_pets_photo_count,
        'pets': pets,
    }
    return render(request, 'main/profile_details.html', context)


# short version of create/edit profile form
def profile_action(request, form_class, success_url, instance, template_name):
    if request.method == 'POST':
        # create the form with POST
        form = form_class(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(success_url)
    else:
        # pull the form with GET
        form = form_class(instance=instance)

    context = {
        'form': form,
    }
    return render(request, template_name, context)


def create_profile(request):
    return profile_action(request, CreateProfileForm, 'dashboard', Profile(), 'main/profile_create.html')


def edit_profile(request):
    return profile_action(request, EditProfileForm, 'profile details', get_profile(), 'main/profile_edit.html')


# longer version of create/edit profile form
# def create_profile(request):
#     if request.method == 'POST':
#         # create the form with POST
#         form = CreateProfileForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         # pull the form with GET
#         form = CreateProfileForm()
#
#     context = {
#         'form': form,
#     }
#     return render(request, 'profile_create.html', context)
#
#
# def edit_profile(request):
#     profile = get_profile()
#     if request.method == 'POST':
#         # create the form with POST
#         form = EditProfileForm(request.POST, instance=profile)
#         if form.is_valid():
#             form.save()
#             return redirect('profile details')
#     else:
#         # pull the form with GET
#         form = EditProfileForm(instance=profile)
#     context = {
#         'form': form
#     }
#
#     return render(request, 'profile_edit.html', context)


def delete_profile(request):
    return profile_action(request, DeleteProfileForm, 'index', get_profile(), 'main/profile_delete.html')
