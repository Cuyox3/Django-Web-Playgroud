from django.utils.translation.template import context_re
from django.views.generic.base import TemplateView
from django.shortcuts import render

class HomePageView(TemplateView):
    template_name = 'core/home.html'

    #def get_context_data(self, **kwargs):
    #    context= super().get_context_data(**kwargs)
    #    context['tittle'] ="Mi super Web "
    #    return context

    def get(self,request, *args, **kwargs):
        return render(request,self.template_name,{'title':"Mi super Web"})

class SamplePageView(TemplateView):
    template_name = 'core/home.html'
