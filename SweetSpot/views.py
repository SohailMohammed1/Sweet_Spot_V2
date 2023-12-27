from django.shortcuts import render, redirect
from .models import DinnerReservation
from .forms import ReservationForm
from django.shortcuts import get_object_or_404

# Create your views here.
def get_sweetspot(request):
    return render(request, 'SweetSpot/base.html')

def add_reservation(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.status = 0  
            reservation.save()
            return redirect('homepage')
    else:
        form = ReservationForm()
    context = {
        'form': form,
        'reservations': DinnerReservation.objects.all()
    }
    return render(request, 'SweetSpot/add_reservation.html', context)