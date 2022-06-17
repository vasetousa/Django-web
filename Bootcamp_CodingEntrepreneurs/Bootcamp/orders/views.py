from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from Bootcamp.orders.forms import OrderForm
from Bootcamp.orders.models import Order
from Bootcamp.products.models import Product


@login_required
def order_checkout_view(request):
    qs = Product.objects.filter(featured=True)
    if not qs.exists():
        return redirect('/')
    product = qs.first()
    ''' @login_required assures the user is not Anonymous!! '''
    user = request.user

    order_id = request.session.get('order_id')
    order_obj = None
    new_creation = False
    try:
        order_obj = Order.objects.get(id=order_id)
    except:
        order_id = None

    if order_id is None:
        new_creation = True
        order_obj = Order.objects.create(product=product, user=user)
    if order_obj is not None and new_creation is False:
        if order_obj.product.id != product.id:
            order_obj = Order.objects.create(product=product, user=user)
    request.session['order_id'] = order_obj.id

    form = OrderForm(request.POST or None,  instance=order_obj)
    if form.is_valid():
        print(form.cleaned_data.get(
            'shipping_address'))
        print(form.cleaned_data.get(
            'billing_address'))

    context = {
        'form': form,
    }
    return render(request, 'forms.html', context)
