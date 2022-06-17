from django.shortcuts import render
from django.views import generic as views

# Create your views here.
from class_based_views.cbv.models import Todo


def index(request):
    context = {
        'title': 'It works with func view',
    }
    return render(request, 'index.html', context)


class IndexView(views.View):
    def get(self, request):
        context = {
            'title': 'It works with class view',
        }
        return render(request, 'index.html', context)

    def post(self, request):
        pass


class IndexTemplateView(views.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'It works with class Templateview'

        return context

#
# class RedirectView(views.RedirectView):
#     # url = reverse_lazy('index class-based')
#
#     def get_redirect_url(self, *args, **kwargs):
#         # if ....:
#         #     return 'place 1'
#         # else:
#         #     return 'place 2 '
#         pass


class TodosListView(views.ListView):
    model = Todo
    template_name = 'todos-list.html'
    ordering = ('title', 'category__name')
    context_object_name = 'todos'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #
    #     return context


class TodosDetailsView(views.DetailView):
    model = Todo
    template_name = 'todos-details.html'
