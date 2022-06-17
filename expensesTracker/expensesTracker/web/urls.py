from django.urls import path

from expensesTracker.web.views import delete_profile, edit_profile, show_profile, delete_expense, edit_expense, \
        create_expense, show_index, create_profile

urlpatterns = (
        path('', show_index, name='show index'),

        path('create/', create_expense, name='create expense'),
        path('edit/<int:pk>/', edit_expense, name='edit expense'),
        path('delete/<int:pk>/', delete_expense, name='delete expense'),

        path('profile/', show_profile, name='show profile'),

        # path to a view created by me (not in the reqs) v
        path('profile/create/', create_profile, name='create profile'),

        path('profile/edit/', edit_profile, name='edit profile'),
        path('profile/delete/', delete_profile, name='delete profile'),
)