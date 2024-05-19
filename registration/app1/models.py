
# app1/models.py
from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=30, default='')
    last_name = models.CharField(max_length=30, default='')
    email = models.EmailField()
    specialization = models.CharField(max_length=100, default='')
    location = models.CharField(max_length=100, default='')
    details = models.TextField(default='')
    profile_picture = models.ImageField(upload_to='doctor_profile_pics/', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.specialization} - {self.location}"
