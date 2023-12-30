from django.contrib import admin
from .models import Dessert


@admin.register(Dessert)
class DessertAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)
