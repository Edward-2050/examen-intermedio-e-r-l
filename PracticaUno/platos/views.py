from django.shortcuts import render
from  platos.models import Platos

# Create your views here.
def plantilla_p(request):
    data_context = Platos.objects.all()
    return render(request, 'plantilla_platos.html',{'data': data_context})
