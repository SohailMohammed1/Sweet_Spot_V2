from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from SweetSpot.models import DinnerReservation


class AccountViewsTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpass123')
        self.user.save()

    def test_signup_view_POST_valid(self):
        form_data = {
            'username': 'newuser',
            'password1': 'testpass123',
            'password2': 'testpass123',
        }
        response = self.client.post(reverse('signup'), data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_signup_view_POST_invalid(self):
        form_data = {
            'username': 'newuser',
            'password1': 'testpass123',
            'password2': 'wrongconfirmation',
        }
        response = self.client.post(reverse('signup'), data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.objects.filter(username='newuser').exists())

    def test_account_options_view(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('account_options'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/options.html')

    def test_profile_view(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/profile.html')

    def test_reservations_list_view(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('sweet_spot'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'SweetSpot/sweet_spot.html')
        self.assertEqual(len(
            response.context['reservations']),
            DinnerReservation.objects.filter(
            ser=self.user).count())

    def tearDown(self):
        self.user.delete()