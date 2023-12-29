from django.test import TestCase, Client
from .models import DinnerReservation
from django.urls import reverse
from django.utils import timezone
from .forms import ReservationForm


class TestViews(TestCase):

    def test_get_reservation_page(self):
        response = self.client.get('/sweet_spot/')    
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'SweetSpot/sweet_spot.html') 

    def test_get_add_item_page(self):
        response = self.client.get('/add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'SweetSpot/add_reservation.html') 

    def test_get_edit_item_page(self):
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
        response = self.client.get(f'/edit/{reservation.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'SweetSpot/edit_reservation.html')

    def test_can_delete_item(self):
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
        response = self.client.get(f'/delete/{reservation.id}/')
        self.assertRedirects(response, '/sweet_spot/')

    