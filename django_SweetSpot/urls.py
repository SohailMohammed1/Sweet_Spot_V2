"""django_SweetSpot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from SweetSpot import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.get_sweetspot, name="homepage"), 
    path('add/', views.add_reservation, name='add_reservation'),
    path('sweet_spot/', views.get_sweet_spot, name='sweet_spot'), 
    path('edit/<int:reservation_id>/', views.edit_reservation, name='edit_reservation'),
    path('toggle/<int:reservation_id>/', views.toggle_reservation, name='toggle_reservation'),
    path('delete/<int:reservation_id>/', views.delete_reservation, name='delete_reservation'),
]


