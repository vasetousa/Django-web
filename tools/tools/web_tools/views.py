import random


# Create your views here.
from django.shortcuts import render
from django.views.decorators.cache import cache_page


@cache_page(10)
def show_index(request):
    value = random.randint(1, 10000)

    context = {
        'value': value
    }
    return render(request, 'show_index.html', context)
