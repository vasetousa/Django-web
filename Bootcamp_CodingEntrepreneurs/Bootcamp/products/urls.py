from django.urls import path

from Bootcamp.accounts.views import login_view, register_view, logout_view
from Bootcamp.orders.views import order_checkout_view
from Bootcamp.products.views import product_create_view

urlpatterns = [
    # path('search', search_view, name='search'),
    path('', product_create_view, name='featured'),

    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='login'),
    path('register/', register_view, name='register'),
    path('checkout/', order_checkout_view, name='checkout'),

]