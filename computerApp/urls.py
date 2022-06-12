#!/bin/python3

from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
    path('add_machine/', views.machine_add_form, name='machine_add'),
    path('machine/<pk>', views.machine_detail_view, name='machine_detail'),
    path('machines/', views.machine_list_view, name='machines'),

    path('add_personnelle/', views.personnelle_add_form, name='personnelle_add'),
    path('personnelle/<pk>', views.personnelle_detail_view, name='personnelle_detail'),
    path('personnelles/', views.personnelle_list_view, name='personnelles'),

    path('add_infrastructure/', views.infrastructure_add_form, name='infrastructure_add'),
    path('infrastructure/<pk>', views.infrastructure_detail_view, name='infrastructure_detail'),
    path('infrastructures/', views.infrastructure_list_view, name='infrastructures'),
]