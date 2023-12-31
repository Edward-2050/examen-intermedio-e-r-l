from django.urls import path
from . import views

urlpatterns = [
    path('plantilla_m/', views.plantilla_m, name='plantilla_m'),
    path('meseros_list_vc/', views.MeserosList.as_view(), name='meseros_list_vc'),
    path('meseros_create_vc/', views.MeserosCreate.as_view(), name='meseros_create_vc'),
    path('meseros_edit_vc/', views.MeserosUpdate.as_view(), name='meseros_edit_vc')
]

