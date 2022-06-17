from django.urls import reverse_lazy
from django.views import generic as views
# from django.shortcuts import render, redirect

from petstagram.main.forms import CreatePetForm, EditPetForm, DeletePetForm
# from petstagram.main.models import Pet
# from petstagram.main.views.helpers import get_profile


# def pet_action(request, form_class, success_url, instance, template_name):
#     if request.method == 'POST':
#         # create the form with POST
#         form = form_class(request.POST, instance=instance)
#         if form.is_valid():
#             form.save()
#             return redirect(success_url)
#     else:
#         # pull the form with GET
#         form = form_class(instance=instance)
#
#     context = {
#         'form': form,
#         'pet': instance,
#     }
#     return render(request, template_name, context)


# def add_pet(request):
#     return pet_action(
#         request,
#         CreatePetForm,
#         'profile details',
#         Pet(user_profile=get_profile()),
#         'pet_create.html'
#     )
#

class AddPetView(views.CreateView):
    form_class = CreatePetForm
    template_name = 'main/pet_create.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    success_url = reverse_lazy('dashboard')


# def edit_pet(request, pk):
#     return pet_action(request, EditPetForm, 'profile details', Pet.objects.get(pk=pk), 'pet_edit.html')

class EditPetView(views.UpdateView):
    form_class = EditPetForm
    template_name = 'main/pet_edit.html'



#
# def delete_pet(request, pk):
#     return pet_action(request, DeletePetForm, 'profile details', Pet.objects.get(pk=pk), 'pet_delete.html')


class DeletePetView(views.DeleteView):
    form_class = DeletePetForm
    template_name = 'main/pet_delete.html'



