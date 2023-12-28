from django.db import models
from django.contrib.auth import get_user_model
from cloudinary.models import CloudinaryField

STATUS = ((0, "draft"), (1, "Published"))


class sweetspotmodel(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

class DinnerReservation(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True, null=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    no_of_guests = models.IntegerField()
    no_of_tables = models.IntegerField(default=0)
    date_selected = models.DateField()
    time_selected = models.TimeField()
    special_request = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS)

    class Meta:
        ordering = ['-created_on']

class Reservation(models.Model):
    # model fields

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def is_available(self): #Logic for user availability for date, time and tables
        reservations = Reservation.objects.filter(date_selected=self.date_selected, time_selected=self.time_selected)
        total_tables_booked = sum(reservation.no_of_tables for reservation in reservations)
        return total_tables_booked + self.no_of_tables <= MAX_TABLES_AVAILABLE

    def save(self, *args, **kwargs):
        if self.is_available():
            super().save(*args, **kwargs)

    def cancel(self): #Logic to all user to cancel reservation
        self.update_status(CANCELLED_STATUS)


    def update_status(self, new_status):
        self.status = new_status
        self.save()

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def send_confirmation_email(self): #Logic to send confirmation email to user
        subject = 'Dinner Reservation Confirmation'
        message = 'Your dinner reservation has been confirmed. Thank you!'
        from_email = 'your-email@example.com'
        to_email = self.email
        send_mail(subject, message, from_email, [to_email])

