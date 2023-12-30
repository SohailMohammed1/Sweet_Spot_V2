# desserts/forms.py

from django import forms
from .models import Dessert

class DessertForm(forms.ModelForm):
    class Meta:
        model = Dessert
        fields = ['name', 'description', 'ingredients', 'instructions']
