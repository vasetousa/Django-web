from django.views import generic as views

from cbv_petstagram.petstagram.forms import CreatePetForm, EditPetForm, DeletePetForm


class CreatePetView(views.CreateView):
    form_class = CreatePetForm
    template_name = 'main/pet_create.html'


class EditPetView(views.UpdateView):
    form_class = EditPetForm
    template_name = 'main/pet_edit.html'


class DeletePetView(views.DeleteView):
    form_class = DeletePetForm
    template_name = 'main/pet_delete.html'
