from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Dessert


class DessertModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username='testuser',
            password='testpassword')
        cls.dessert = Dessert.objects.create(
            user=cls.user,
            name='Chocolate Cake',
            description='A rich chocolate cake.',
            ingredients='Cocoa, Flour, Sugar, Eggs, Butter',
            instructions='Preheat oven, mix ingredients, bake for 35 minutes.',
        )

    def test_dessert_creation(self):
        self.assertTrue(isinstance(self.dessert, Dessert))
        self.assertEqual(self.dessert.__str__(), 'Chocolate Cake')

    def test_dessert_string_representation(self):
        self.assertEqual(str(self.dessert), 'Chocolate Cake')

    def test_dessert_created_at(self):
        now = timezone.now()
        self.assertLess(self.dessert.created_at, now)

    def test_dessert_updated_at(self):
        now = timezone.now()
        self.assertLessEqual(self.dessert.updated_at, now)

    def test_user_foreign_key(self):
        self.assertEqual(self.dessert.user, self.user)

    def test_dessert_update(self):
        self.dessert.name = 'Updated Name'
        self.dessert.save()
        updated_dessert = Dessert.objects.get(pk=self.dessert.pk)
        self.assertEqual(updated_dessert.name, 'Updated Name')
        now = timezone.now()
        self.assertLessEqual(updated_dessert.updated_at, now)