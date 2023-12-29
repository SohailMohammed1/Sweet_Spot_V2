from django.test import TestCase, Client
from .models import DinnerReservation
from django.urls import reverse
from django.utils import timezone
from .forms import ReservationForm


class TestViews(TestCase):

    
    def setUp(self):
        # Set up the test environment before each test method runs
        self.reservation = DinnerReservation.objects.create(
            first_name='Test',
            last_name='User',
            email='test@example.com',
            phone_number='1234567890',
            no_of_guests=2,
            date_selected=timezone.now().date(),
            time_selected=timezone.now().time(),
            special_request='Initial request',
            status=0
        )
        self.edit_url = reverse('edit_reservation', args=[self.reservation.id])

    def test_get_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'SweetSpot/base.html')

    def test_get_reservation_page(self):
        response = self.client.get('/sweet_spot/')    
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'SweetSpot/sweet_spot.html') 

    def test_get_add_reservation_page(self):
        response = self.client.get('/add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'SweetSpot/add_reservation.html') 

    def test_get_edit_reservation_page(self):
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

    def test_item_string_method_returns_name(self):
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
        self.assertEqual(str(reservation), 'Test Reservation')

    def test_add_reservation_POST_valid_data(self):
        post_data = {
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'testuser@example.com',
            'phone_number': '1234567890',
            'no_of_guests': 4,
            'date_selected': timezone.now().date(),
            'time_selected': timezone.now().time(),
            'special_request': 'No onions',
            
        }
        response = self.client.post('/add/', data=post_data)

        self.assertEqual(response.status_code, 302) 
        self.assertRedirects(response, reverse('sweet_spot'))  
         

        
        reservation = DinnerReservation.objects.first()
        self.assertEqual(reservation.first_name, 'Test')
        self.assertEqual(reservation.status, 0)

    def test_edit_reservation_POST_valid_data(self):
        post_data = {
            'first_name': 'Updated',
            'last_name': 'User',
            'email': 'updated@example.com',
            'phone_number': '0987654321',
            'no_of_guests': 3,
            'date_selected': timezone.now().date(),
            'time_selected': timezone.now().time(),
            'special_request': 'Updated request',
            'status': 0
        }
        response = self.client.post(f'/edit/{self.reservation.id}/', data=post_data)
        
        self.reservation.refresh_from_db()

        self.assertEqual(self.reservation.first_name, 'Updated')
        self.assertEqual(self.reservation.email, 'updated@example.com')
        self.assertEqual(self.reservation.special_request, 'Updated request')

        self.assertRedirects(response, reverse('sweet_spot'))