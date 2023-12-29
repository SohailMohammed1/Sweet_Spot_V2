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
from accounts import views as account_views
from django.contrib.auth import views as auth_views
from django.contrib.auth import views as user_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.get_sweetspot, name="homepage"), 
    path('add/', views.add_reservation, name='add_reservation'),
    path('sweet_spot/', views.get_sweet_spot, name='sweet_spot'), 
    path('edit/<int:reservation_id>/', views.edit_reservation, name='edit_reservation'),
    path('delete/<int:reservation_id>/', views.delete_reservation, name='delete_reservation'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', account_views.signup, name='signup'),
]


