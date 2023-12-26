from django.shortcuts import render, redirect
from .models import DinnerReservation
from .forms import ReservationForm
from django.shortcuts import get_object_or_404


def get_sweet_spot(request):
    reservations = DinnerReservation.objects.all().order_by('id')  
    context = {
        'reservations': reservations
    }
    return render(request, 'sweet_spot/sweet_spot.html', context)

def add_reservation(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.status = 0  
            reservation.save()
            return redirect('sweet_spot')
    else:
        form = ReservationForm()
    context = {
        'form': form,
        'reservations': DinnerReservation.objects.all()
    }
    return render(request, 'sweet_spot/add_reservation.html', context)


def edit_reservation(request, reservation_id):
    reservation = get_object_or_404(DinnerReservation, pk=reservation_id)
    if request.method == "POST":
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('sweet_spot')
    else:
        form = ReservationForm(instance=reservation)
    context = {
        'form': form
    }
    return render(request, 'sweet_spot/edit_reservation.html', context)

def toggle_reservation(request, reservation_id):
    reservation = get_object_or_404(DinnerReservation, pk=reservation_id)
    reservation.status = not reservation.status
    reservation.save()
    return redirect('sweet_spot')

def delete_reservation(request, reservation_id):
    reservation = get_object_or_404(DinnerReservation, pk=reservation_id)
    reservation.delete()
    return redirect('sweet_spot') 

