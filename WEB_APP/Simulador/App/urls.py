from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('file',views.archivos,name='archivos'),
    path('peticion',views.peticiones,name='peticiones'),
    path('ayuda',views.ayuda,name='ayuda')
]

if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )