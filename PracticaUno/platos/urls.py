from django.urls import path
from .import views

urlpatterns = [
    path('pantilla_p/', views.plantilla_p, name='plantillas_p'),
]