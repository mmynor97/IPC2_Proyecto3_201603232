from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('archivos/',views.archivos,name='archivos'),
    path('peticiones/',views.peticiones,name='peticiones'),
    path('ayuda/',views.ayuda,name='ayuda')
]
