from django.contrib import admin
from SweetSpot.models import DinnerReservation
from django_summernote.admin import SummernoteModelAdmin

@admin.register(DinnerReservation)
class DinnerReservationAdmin(SummernoteModelAdmin):

    list_display = ('first_name', 'last_name', 'slug', 'status', 'created_on')
    search_fields = ['first_name', 'content']
    prepopulated_fields = {'slug': ('first_name',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')

    