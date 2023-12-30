from django.db import models
from django.contrib.auth import get_user_model
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

STATUS = ((0, "draft"), (1, "Published"))


class sweetspotmodel(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

class DinnerReservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
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
    done = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ['-created_on']

