from django.urls import path
from . import views

urlpatterns = [
    path('plantilla_m/', views.plantilla_m, name='plantilla_m'),
]