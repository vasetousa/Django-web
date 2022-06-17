from django.urls import path

from class_based_views.cbv.views import IndexView, index, IndexTemplateView, TodosListView, \
    TodosDetailsView

urlpatterns = [
    path('fbv/', index, name='index func-based'),
    path('cbv/', IndexView.as_view(), name='index class-based'),
    path('cbv-template/', IndexTemplateView.as_view(), name='index class-based (template)'),
    path('todos/', TodosListView.as_view(), name='todos list'),
    path('todos/<int:pk>/', TodosDetailsView.as_view(), name='todos details'),
    ]
