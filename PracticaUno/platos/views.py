from django.shortcuts import render

# Create your views here.
def plantilla_p(request):
    return render(request, 'plantilla_platos.html',{})