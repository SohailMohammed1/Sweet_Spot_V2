from django.test import TestCase, Client
from .models import DinnerReservation
from django.urls import reverse
from django.utils import timezone
from .forms import ReservationForm

class TestReservationForm(TestCase):
    def test_field_first_name_is_required(self):
        form = ReservationForm({'first_name':''})
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors.keys())
        self.assertEqual(form.errors['first_name'][0], 'This field is required.') 

    def test_field_last_name_is_required(self):
        form = ReservationForm({'last_name':''})
        self.assertFalse(form.is_valid())
        self.assertIn('last_name', form.errors.keys())
        self.assertEqual(form.errors['last_name'][0], 'This field is required.') 

    def test_field_email_is_required(self):
        form = ReservationForm({'email':''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'This field is required.')

    def test_field_email_is_required(self):
        form = ReservationForm({'phone_number':''})
        self.assertFalse(form.is_valid())
        self.assertIn('phone_number', form.errors.keys())
        self.assertEqual(form.errors['phone_number'][0], 'This field is required.')

    def test_field_number_of_guests_is_required(self):
        form = ReservationForm({'no_of_guests':''})
        self.assertFalse(form.is_valid())
        self.assertIn('no_of_guests', form.errors.keys())
        self.assertEqual(form.errors['no_of_guests'][0], 'This field is required.')

    def test_field_date_is_required(self):
        form = ReservationForm({'date_selected':''})
        self.assertFalse(form.is_valid())
        self.assertIn('date_selected', form.errors.keys())
        self.assertEqual(form.errors['date_selected'][0], 'This field is required.')

    def test_field_time_is_required(self):
        form = ReservationForm({'time_selected':''})
        self.assertFalse(form.is_valid())
        self.assertIn('time_selected', form.errors.keys())
        self.assertEqual(form.errors['time_selected'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ReservationForm()
        self.assertEqual(form.Meta.fields, ['first_name', 'last_name', 'email', 'phone_number', 'no_of_guests', 
            'date_selected', 'time_selected', 'special_request'])
