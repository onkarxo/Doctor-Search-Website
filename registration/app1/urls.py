# app1/urls.py
from django.urls import path
from .views import add_doctor,doctor_detail,home, index,contact

from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('doctor/<int:doctor_id>/', doctor_detail, name='doctor_detail'),    
    path('add_doctor/', add_doctor, name='add_doctor'),
    path('doctors', home, name='home'),
    path('contact/', contact, name='contact'),
    
]