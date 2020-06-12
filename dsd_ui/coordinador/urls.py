from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('iniciar', views.index, name='index'),
    path('execute_server', views.execute_server, name='execute')
]