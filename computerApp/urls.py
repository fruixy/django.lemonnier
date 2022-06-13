#!/bin/python3

from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
    path('add_machine/', views.machine_add_form, name='machine_add'),
    path('machines/', views.machine_list_view, name='machines'),
    path('machine_remove/<id>',views.machine_remove, name='machine_remove'),

    path('add_personnelle/', views.personnelle_add_form, name='personnelle_add'),
    path('personnelles/', views.personnelle_list_view, name='personnelles'),
    path('personnelle_remove/<id>',views.personnelle_remove, name='personnelle_remove'),

    path('add_infrastructure/', views.infrastructure_add_form, name='infrastructure_add'),
    path('infrastructures/', views.infrastructure_list_view, name='infrastructures'),
    path('infrastructure_remove/<id>',views.infrastructure_remove, name='infrastructure_remove'),
]