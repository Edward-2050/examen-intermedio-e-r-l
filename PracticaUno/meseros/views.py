from django.shortcuts import render

# Create your views here.
def plantilla_m(request):
    return render(request, 'plantilla_meseros.html',{})