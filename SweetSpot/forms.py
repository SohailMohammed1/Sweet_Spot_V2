from django import forms
from .models import DinnerReservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = DinnerReservation
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'no_of_guests', 'date_selected', 'time_selected', 'special_request']