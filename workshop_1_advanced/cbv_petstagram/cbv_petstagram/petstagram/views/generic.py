from django.shortcuts import render, redirect
from django.views import generic as views

from cbv_petstagram.petstagram.models import PetPhoto


class HomeView(views.TemplateView):
    template_name = 'main/home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_nav_items'] = True
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return super().dispatch(request, *args, **kwargs)


class DashboardView(views.ListView):
    model = PetPhoto
    template_name = 'main/dashboard.html'
    context_object_name = 'pet_photos'


# def show_dashboard(request):
#     profile = get_profile()
#     if not profile:
#         return redirect('error 401')
#
#     profile = get_profile()
#     pet_photos = PetPhoto.objects\
#         .prefetch_related('tagged_pets')\
#         .filter(tagged_pets__user_profile=profile)\
#         .distinct()
#
#     context = {
#         'pet_photos': pet_photos,
#     }
#
#     return render(request, 'main/dashboard.html', context)


def error_401(request):
    return render(request, 'main/401_error.html')
