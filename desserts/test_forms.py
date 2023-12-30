from django.test import TestCase
from .forms import DessertForm
from .models import Dessert
from django.contrib.auth.models import User


class DessertFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
            )

    def test_dessert_form_fields(self):
        form = DessertForm()
        self.assertEqual(set(form.fields), set(
            ['name',
                'description',
                'ingredients',
                'instructions']))

    def test_dessert_form_valid_data(self):
        form_data = {
            'name': 'Chocolate Cake',
            'description': 'Rich chocolate sponge',
            'ingredients': 'Cocoa, Eggs, Flour, Sugar',
            'instructions': 'Mix ingredients, bake at 180°C for 35 minutes.'
        }
        form = DessertForm(data=form_data)
        self.assertTrue(form.is_valid())
        dessert = form.save(commit=False)
        dessert.user = self.user
        dessert.save()
        self.assertEqual(Dessert.objects.count(), 1)
        self.assertEqual(Dessert.objects.first().name, 'Chocolate Cake')

    def test_dessert_form_invalid_data(self):
        form_data = {
            'name': '',
            'description': 'No name provided',
            'ingredients': 'Cocoa, Eggs, Flour, Sugar',
            'instructions': 'Mix ingredients, bake at 180°C for 35 minutes.'
        }
        form = DessertForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)

    def test_dessert_form_partial_data(self):
        form_data = {
            'name': 'Lemon Tart',
            'ingredients': 'Lemon, Sugar, Butter, Flour',
            'instructions': 'Mix ingredients, bake at 175°C for 45 minutes.'
        }
        form = DessertForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors)