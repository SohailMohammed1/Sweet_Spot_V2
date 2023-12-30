from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from SweetSpot.models import DinnerReservation
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('homepage')  
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def account_options(request):
    return render(request, 'accounts/options.html')

def profile(request):
    return render(request, 'accounts/profile.html')

@login_required
def reservations_list(request):
    user_reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'SweetSpot/Sweet_Spot.html', {'reservations': user_reservations})
