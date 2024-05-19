# app1/forms.py
from django import forms
from .models import Doctor

class DoctorForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    location = forms.CharField(max_length=100)
    details = forms.Textarea()
    profile_picture = forms.ImageField(required=False)

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
    
    ]
    specialization = forms.ChoiceField(choices=SPECIALIZATION_CHOICES)

    class Meta:
        model = Doctor
        fields = [ 'first_name', 'last_name','email', 'specialization', 'location', 'details', 'profile_picture']
