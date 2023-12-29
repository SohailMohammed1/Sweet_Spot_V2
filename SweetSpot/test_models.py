from django.test import TestCase, Client
from .models import DinnerReservation
from django.urls import reverse
from django.utils import timezone
from .forms import ReservationForm

class TestModels(TestCase):

    def test_done_defaults_to_false(self):
        reservation = DinnerReservation.objects.create(
            first_name='Test',
            last_name='Reservation',
            email='test@example.com',
            phone_number='1234567890',
            no_of_guests=2,
            date_selected=timezone.now().date(),
            time_selected=timezone.now().time(),
            special_request='Hot Dogs',
            status=0  
        )
        self.assertFalse(reservation.done) 