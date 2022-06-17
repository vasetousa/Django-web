'''
Class Based Views
from django.views import generic as views
    Generic views
1. Base Views
    - 'View' class gives us the branching in the func based views. Use class method 'as.view()'
    in urls.py, which have inside method 'view'. It returns a function
    - 'TemplateView' class inherits from 'TemplateView, TemplateResponseMixin, ContextMixin, View'
    - 'RedirectView' class inherits from 'View' class. You may not create class view, but
    point the url directly in the urls.py. ex. path('example-some url', 'RedirectView.as_view(url='some-url')
    - 'List View'
    - 'Details View'
    - 'Crud Views'   1:55:40






'''