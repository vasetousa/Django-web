from django.urls import path

from tasks.cbv_tasks.views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView, \
    RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),

    path('', TaskList.as_view(), name='all tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task details'),
    path('task_create/', TaskCreate.as_view(), name='task create'),
    path('task_update/<int:pk>/', TaskUpdate.as_view(), name='task update'),
    path('task_delete/<int:pk>/', TaskDelete.as_view(), name='task delete'),
]