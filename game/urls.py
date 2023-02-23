from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('proceso',views.proceso,name='proceso'),
    path('suma',views.suma,name='suma'),
    path('bienvenida',views.bienvenida,name='bienvenida'),
    path('multiplicacion',views.multiplicacion, name='multiplicacion'),
    path('division',views.division, name='division'),
]