from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from desserts.models import Dessert  
from desserts.forms import DessertForm  

class DessertViewsTest(TestCase):
    def setUp(self):
        # Create a user and log them in
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        
        # Create a Dessert instance for use in tests
        self.dessert = Dessert.objects.create(name='Test Dessert', user=self.user)
        
    def test_list_desserts(self):
        response = self.client.get(reverse('list_desserts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'desserts/dessert_list.html')
        self.assertIn('desserts', response.context)
        self.assertEqual(list(response.context['desserts']), list(Dessert.objects.all()))

    def test_add_dessert_get(self):
        response = self.client.get(reverse('add_dessert'))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], DessertForm)
        self.assertTemplateUsed(response, 'desserts/add_dessert.html')

    def test_add_dessert_post_success(self):
        dessert_count = Dessert.objects.count()
        response = self.client.post(reverse('add_dessert'), {'name': 'New Dessert'})
        self.assertEqual(Dessert.objects.count(), dessert_count + 1)
        self.assertRedirects(response, reverse('list_desserts'))

    def test_add_dessert_post_failure(self):
        dessert_count = Dessert.objects.count()
        response = self.client.post(reverse('add_dessert'), {'name': ''}) 
        self.assertEqual(Dessert.objects.count(), dessert_count)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['form'].errors)

    def test_edit_dessert_get(self):
        response = self.client.get(reverse('edit_dessert', kwargs={'pk': self.dessert.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'desserts/edit_dessert.html')
        self.assertIsInstance(response.context['form'], DessertForm)

    def test_edit_dessert_post_success(self):
        # Send POST data that includes all required fields
        post_data = {
            'name': 'Updated Dessert',
            # Include other fields here if necessary
        }
        response = self.client.post(reverse('edit_dessert', kwargs={'pk': self.dessert.pk}), post_data)

        # Make sure the response is redirecting to the correct URL
        self.assertRedirects(response, reverse('list_desserts'))

        # Reload the dessert from the database
        self.dessert.refresh_from_db()

        # Assert the name has been updated
        self.assertEqual(self.dessert.name, 'Updated Dessert')

    def test_delete_dessert(self):
        dessert_count = Dessert.objects.count()
        response = self.client.post(reverse('delete_dessert', kwargs={'pk': self.dessert.pk}))
        self.assertEqual(Dessert.objects.count(), dessert_count - 1)
        self.assertRedirects(response, reverse('list_desserts'))

    # Add tearDown method if needed to clean up after tests

