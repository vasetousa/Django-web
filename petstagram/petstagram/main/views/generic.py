from django.views import generic as views
from django.shortcuts import render, redirect
from petstagram.main.views.helpers import get_profile
from petstagram.main.models import PetPhoto

'''
Function based view same as Class based view below, change in urls too
'''


# def show_home(request):
#     context = {
#         'hide_nav_items': True,
#     }
#
#     return render(request, 'main/home_page.html', context)


class HomeView(views.TemplateView):
    template_name = 'main/home_page.html'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['hide_nav_items'] = True
        return contex

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')

        return super().dispatch(request, *args, **kwargs)


'''
Function based view same as Class based view below, change in urls too
'''


# def show_dashboard(request):
#     profile = get_profile()
#     pet_photos = set(PetPhoto.objects.filter(tagged_pets__user_profile=profile))
#
#     context = {
#         'pet_photos': pet_photos,
#     }
#
#     return render(request, 'main/dashboard.html', context)
#

class DashboardView(views.ListView):
    model = PetPhoto
    template_name = 'main/dashboard.html'
    context_object_name = 'pet_photos'
