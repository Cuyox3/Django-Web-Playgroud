from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView, FormView
from django.urls import reverse, reverse_lazy
from .models import Page

# Create your views here.
class PageListView(ListView):
    model = Page

class PageDetailView(DetailView):
    model = Page

class PageCreateView(CreateView):
    model = Page
    fields = ('title', 'content','order')
    success_url = reverse_lazy('pages:pages')

class PageUpdateView(UpdateView):
    model = Page
    fields = ('title', 'content','order')
    template_name_suffix = '_update_form'

    def get_success_url(self): #Se puede hacer pero es de gente no floja
        return reverse_lazy('pages:update',args=[self.object.id]) + '?ok'

class PageDeleteView(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')