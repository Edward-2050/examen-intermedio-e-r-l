from django.shortcuts import render
from meseros.models import Meseros
from django.urls import  reverse_lazy
from  django.views.generic import ListView, CreateView, UpdateView, DeleteView
from meseros.forms import MeserosForm

# Create your views here.
def plantilla_m(request):
    data_context = Meseros.objects.all()
    return render(request, 'plantilla_meseros.html',{'data' : data_context})

class MeserosList(ListView):
    model = Meseros
    template_name = 'meseros_list_vc.html'

class MeserosCreate(CreateView):
    model = Meseros
    form_class = MeserosForm
    template_name = 'meseros_create.html'
    success_url = reverse_lazy('meseros_create_vc')

class MeserosUpdate(UpdateView):
    model = Meseros
    form_class = MeserosForm
    template_name = 'meseros_update_vc.html'
    success_url = reverse_lazy('meseros_create_vc')