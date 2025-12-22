from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator 
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import Page  # Asegúrate de importar tu modelo Page
from .forms import PageForm

class StaffRequaredmixin(object): 
    """
    Este mixin requerira que el usuaria sea parte del staff    
    """
    @method_decorator (staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        #print (request.user)
        #if not request.user.is_staff:
        #    return redirect (reverse_lazy('admin:login'))
        return super(StaffRequaredmixin,self).dispatch(request, *args, **kwargs)

class PageListView(ListView):
    """
    Vista para mostrar una lista de páginas.
    """
    model = Page  # Indica que esta vista trabaja con el modelo 'Page'

class PageDetailView(DetailView):
    """
    Vista para mostrar los detalles de una página específica.
    """
    model = Page  # Indica que esta vista trabaja con el modelo 'Page'

@method_decorator(staff_member_required,name ='dispatch')
class PageCreateView(StaffRequaredmixin, CreateView):
    """
    Vista para crear una nueva página.
    """
    model = Page  # Indica que esta vista trabaja con el modelo 'Page'
    form_class = PageForm # Tiene que ser exactamente este mismo nombre 
    #fields = ('title', 'content', 'order')
    success_url = reverse_lazy('pages:pages')  # URL a la que redirigir después de crear la página

   
class PageUpdateView(UpdateView):
    """
    Vista para actualizar una página existente.
    """
    model = Page  # Indica que esta vista trabaja con el modelo 'Page'
    form_class = PageForm
    #fields = ('title', 'content', 'order')  # Campos del modelo que se mostrarán en el formulario
    template_name_suffix = '_update_form'  # Sufijo para el nombre de la plantilla

    def get_success_url(self):  # Método para obtener la URL de redirección
        """
        Redirige a la página de actualización con un parámetro 'ok'
        para indicar que la actualización fue exitosa.
        """
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'  # Construye la URL con el ID de la página

class PageDeleteView(DeleteView):
    """
    Vista para eliminar una página.
    """
    model = Page  # Indica que esta vista trabaja con el modelo 'Page'
    success_url = reverse_lazy('pages:pages')  # URL a la que redirigir después de eliminar la página