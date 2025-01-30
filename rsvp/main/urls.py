from django.urls import path
from . import views

urlpatterns = [
    path('verify', views.home, name="home"),
    path('verify/guests/', views.guests, name='guests'),
    path('verify/submit/', views.submit_attendee, name='submit_attendee')
]