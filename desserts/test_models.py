from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Dessert

class DessertModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up a user and a dessert for all test methods
        cls.user = User.objects.create_user(username='testuser', password='testpassword')
        cls.dessert = Dessert.objects.create(
            user=cls.user,
            name='Chocolate Cake',
            description='A rich chocolate cake.',
            ingredients='Cocoa, Flour, Sugar, Eggs, Butter',
            instructions='Preheat oven, mix ingredients, bake for 35 minutes.',
        )

    def test_dessert_creation(self):
        # Check if the dessert was created successfully
        self.assertTrue(isinstance(self.dessert, Dessert))
        self.assertEqual(self.dessert.__str__(), 'Chocolate Cake')

    def test_dessert_string_representation(self):
        # The string representation should be equal to the name of the dessert
        self.assertEqual(str(self.dessert), 'Chocolate Cake')

    def test_dessert_created_at(self):
        # The created_at field should be automatically set to the current date/time
        now = timezone.now()
        self.assertLess(self.dessert.created_at, now)

    def test_dessert_updated_at(self):
        # The updated_at field should be automatically set to the current date/time
        now = timezone.now()
        self.assertLessEqual(self.dessert.updated_at, now)  # updated_at should be less or equal to 'now' since it's auto_now

    def test_user_foreign_key(self):
        # The dessert's user should be the user created in setUpTestData
        self.assertEqual(self.dessert.user, self.user)

# You may also want to test the update functionality to check updated_at changes
    def test_dessert_update(self):
        # Update the dessert
        self.dessert.name = 'Updated Name'
        self.dessert.save()

        # Fetch the updated dessert from the database
        updated_dessert = Dessert.objects.get(pk=self.dessert.pk)

        # Check if the dessert name was updated
        self.assertEqual(updated_dessert.name, 'Updated Name')

        # The updated_at field should be changed to the current date/time after update
        now = timezone.now()
        self.assertLessEqual(updated_dessert.updated_at, now)  # Check if updated_at is now
