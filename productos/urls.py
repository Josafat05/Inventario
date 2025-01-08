from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('agregar/', views.agregar_producto, name='agregar_producto'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('nuevo/', views.nuevo_dispositivo, name='nuevo_dispositivo'),
]
