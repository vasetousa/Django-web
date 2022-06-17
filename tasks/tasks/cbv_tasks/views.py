from django.contrib.auth import forms, login
from django.contrib.auth import mixins as auth_mixin
from django.contrib.auth import views as auth_view
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as views

from tasks.cbv_tasks.models import Task


# Create your views here.
class CustomLoginView(auth_view.LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('all tasks')


# form for registering the user in our app
class RegisterPage(views.FormView):
    template_name = 'register.html'
    form_class = forms.UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('all tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    # this method assures any attempt of logged-in user to directly access 'login' page
    # for example is not permitted
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('all tasks')
        return super(RegisterPage, self).get(*args, **kwargs)


class TaskList(auth_mixin.LoginRequiredMixin, views.ListView):
    model = Task
    template_name = 'all_tasks.html'
    context_object_name = 'tasks'
    # paginate_by = 5
    ordering = ['-create']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)  # only user owned items
        context['count'] = context['tasks'].filter(complete=False).count()  # count the complete tasks

        # search field filtering
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__startswith=search_input)

        context['search_input'] = search_input
        return context


class TaskDetail(auth_mixin.LoginRequiredMixin, views.DetailView):
    model = Task
    template_name = 'task_details.html'
    context_object_name = 'task'
    # pk_url_kwarg = 'custom_pk'  # if you want to change 'pk' to 'custom_pk'


# specify the fields unless you want the default ones
class TaskCreate(auth_mixin.LoginRequiredMixin, views.CreateView):
    model = Task
    fields = ['title', 'description', 'complete']
    template_name = 'task_create.html'
    success_url = reverse_lazy('all tasks')

    # form_class = Task   # our model form

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(auth_mixin.LoginRequiredMixin, views.UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    template_name = 'task_update.html'
    success_url = reverse_lazy('all tasks')


class TaskDelete(auth_mixin.LoginRequiredMixin, views.DeleteView):
    model = Task
    template_name = 'task_delete.html'
    success_url = reverse_lazy('all tasks')  # html file to create later
