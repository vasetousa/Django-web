from django.contrib.auth import mixins as auth_mixins
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from petstagram.main.views.helpers import get_profile
from petstagram.main.models import PetPhoto


# def show_pet_photo_details(request, pk):
#     # pet_photo = PetPhoto.objects.get(id=pk) same as below
#     pet_photo = PetPhoto.objects.prefetch_related('tagged_pets').get(pk=pk)
#
#     context = {
#         'pet_photo': pet_photo,
#     }
#
#     return render(request, 'main/photo_details.html', context)

class PetPhotoDetailsView(auth_mixins.LoginRequiredMixin, views.DetailView):
    model = PetPhoto
    template_name = 'main/photo_details.html'
    context_object_name = 'pet_photo'

    def get_queryset(self):
        return super() \
            .get_queryset() \
            .prefetch_related('tagged_pets')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.object.user == self.request.user

        return context


class AddPetPhotoView(auth_mixins.LoginRequiredMixin, views.CreateView):
    model = PetPhoto
    template_name = 'main/photo_create.html'
    fields = ('pet_picture', 'description', 'tagged_pets')

    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def like_pet_photo(request, pk):
    pet_photo = PetPhoto.objects.get(pk=pk)
    pet_photo.likes += 1
    pet_photo.save()
    return redirect('pet photo details', pk)


def add_pet_photo(request):
    return render(request, 'main/photo_create.html')


def edit_pet_photo(request):
    return render(request, 'main/photo_edit.html')
