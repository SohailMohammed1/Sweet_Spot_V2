from django.test import TestCase
from .forms import ReservationForm

class ReservationFormTest(TestCase):

    # Special requirements
    def with_special_request(self):
        form_data = {
            'first_name': 'John',
            'last_name': 'Smith',
            'email': 'john@example.com',
            'phone_number': '1234567890',
            'no_of_guests': 2,
            'date_selected': '2023-12-28',
            'time_selected': '19:00',
            'special_request': 'A table by the window, please.',
        }
        form = ReservationForm(data=form_data)
        self.assertTrue(form.is_valid())


    # No special requirement
    def without_special_request(self):
        form_data = {
            'first_name': 'John',
            'last_name': 'Smith',
            'email': 'john@example.com',
            'phone_number': '0987654321',
            'no_of_guests': 4,
            'date_selected': '2023-12-27',
            'time_selected': '20:00',

        }
        form = ReservationForm(data=form_data)
        self.assertTrue(form.is_valid())

