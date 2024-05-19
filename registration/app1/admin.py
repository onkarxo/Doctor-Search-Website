# app1/admin.py
from django import forms
from django.contrib import admin
from .models import Doctor

class DoctorAdminForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'

    SPECIALIZATION_CHOICES = [
        ('Cardiologist', 'Cardiologist'),
        ('Dermatologist', 'Dermatologist'),
        ('Endocrinologist', 'Endocrinologist'),
        ('Orthopediologist', 'Orthopediologist'),
        ('Pediatrician', 'Pediatrician'),
        ('Neurologist', 'Neurologist'),
        ('Oncologist', 'Oncologist'),
        ('Gastroenterologist', 'Gastroenterologist'),
        ('Psychiatrist', 'Psychiatrist'),
        ('Urologist', 'Urologist'),
        ('ENT Specialist', 'ENT Specialist'),
        ('Ophthalmologist', 'Ophthalmologist'),
        ('Rheumatologist', 'Rheumatologist'),
        ('Allergist', 'Allergist'),
        # Add more specializations as needed
    ]
    specialization = forms.ChoiceField(choices=SPECIALIZATION_CHOICES)

class DoctorAdmin(admin.ModelAdmin):
    form = DoctorAdminForm
    list_display = ('first_name', 'last_name', 'specialization', 'location')
    list_filter = ('specialization', 'location')

admin.site.register(Doctor, DoctorAdmin)
