from django.contrib.auth import mixins as auth_mixins
from django.shortcuts import render, redirect
from django.views import generic as views

from petstagram.main.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
from petstagram.main.models import Profile, PetPhoto, Pet
from petstagram.main.views.helpers import get_profile


class ProfileDetailsView(views.DetailView):
    model = Profile
    template_name = 'main/profile_details.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        pets = list(Pet.objects.filter(user=self.object.user.id))

        pet_photos = PetPhoto.objects\
            .filter(tagged_pets__in=pets)\
            .distinct()

        total_likes_count = sum(pp.likes for pp in pet_photos)

        total_pets_photo_count = len(pet_photos)

        context.update({
            'total_likes_count': total_likes_count,
            'total_pets_photo_count': total_pets_photo_count,
            'pets': pets,
        })
        return context


# def show_profile(request):
#     profile = get_profile()
#     pets = list(Pet.objects.filter(user_profile=profile))
#     total_likes_count = sum(pp.likes for pp in PetPhoto.objects
#                             .filter(tagged_pets__user_profile=profile) \
#                             .distinct()
#                             )
#
#     total_pets_photo_count = len(PetPhoto.objects
#                                  .filter(tagged_pets__user_profile=profile) \
#                                  .distinct()
#                                  )
#
#     context = {
#         'profile': profile,
#         'total_likes_count': total_likes_count,
#         'total_pets_photo_count': total_pets_photo_count,
#         'pets': pets,
#     }
#     return render(request, 'main/profile_details.html', context)
#

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
    return profile_action(request, CreateProfileForm, 'index', Profile(), 'profile_create.html')


def edit_profile(request):
    return profile_action(request, EditProfileForm, 'profile details', get_profile(), 'profile_edit.html')


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
    return profile_action(request, DeleteProfileForm, 'index', get_profile(), 'profile_delete.html')
