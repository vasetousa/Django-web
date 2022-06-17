from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth.decorators import login_required

# Create your views here.
# def search_view(request, *args, **kwargs):
#     return render(request, 'home_page.html')


# def featured_product_view(request, *args, **kwargs):
#     qs = Product.objects.filter(featured=True)
#     product = None
#     form = None
#     can_order = False
#     if qs.exists():
#         product = qs.first()
#     if product != None:
#         can_order = product.can_order
#         if can_order:  # ()
#             product_id = product.id
#             request.session['product_id'] = product_id
#         form = InventoryWaitlistForm(request.POST or None, product=product)
#         if form.is_valid():
#             obj = form.save(commit=False)
#             obj.product = product
#             if request.user.is_authenticated:  # ()
#                 obj.user = request.user
#             obj.save()
#             return redirect("/waitlist-success")
#     context = {
#         "object": product,
#         "can_order": can_order,
#         "form": form,
#     }
#     return render(request, "products/detail.html", context)

#
# def search_view(request, *args, **kwargs):  # /search/
#     # print(args, kwargs)
#
#     query = request.GET.get('q')  # q
#     qs = Product.objects.filter(title__icontains=query[0])
#     print(query, qs)
#     context = {"name": "abc", "query": query}
#     return render(request, "home.html", context)
from Bootcamp.products.forms import DataForm


@staff_member_required
def product_create_view(request):
    form = DataForm(request.POST or None)
    # data = form.cleaned_data()
    if form.is_valid():
        obj = form.save(commit=False)
        # do something else if you want
        obj.save()

        form = DataForm()
    context = {
        'form': form,
    }
    return render(request, 'home_page.html', context)

# class ProductCreateView(views.FormView):
#     model = Product
#     template_name = 'home_page.html'
#     context_object_name = 'products'
#     fields = ['title', 'content']
#     success_url = reverse_lazy('create')
#
#     def form_valid(self, form):
#         return super(ProductCreateView, self).form_valid(form)
