from django.shortcuts import render, redirect, get_object_or_404
from .forms import DoctorForm
from .models import Doctor
from django.contrib import messages

def add_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES)
        if form.is_valid():
            # Create a Doctor instance without associating it with a specific user
            doctor = form.save(commit=False)
            
            # Save the doctor without a user
            doctor.save()

            # Add a success message
            messages.success(request, 'Doctor added successfully!')

            # Redirect to the same add_doctor page
            return redirect('add_doctor')

    else:
        form = DoctorForm()

    return render(request, 'add_doctor.html', {'form': form})

def index(request):
    return render(request, 'index.html')

def home(request):
    specialization_choices = DoctorForm.SPECIALIZATION_CHOICES

    if request.method == 'GET':
        location = request.GET.get('location', '')
        specialization = request.GET.get('specialization', '')
        
        doctors = Doctor.objects.all()

        if location:
            doctors = doctors.filter(location__icontains=location)

        if specialization:
            doctors = doctors.filter(specialization__icontains=specialization)

        context = {
            'doctors': doctors,
            'specialization_choices': specialization_choices,
        }
        return render(request, 'home.html', context)
    
    
def doctor_detail(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    context = {'doctor': doctor}
    return render(request, 'doctor_detail.html', context)

def contact(request):
    
    return render(request, 'contact.html')









