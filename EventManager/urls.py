from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('event_register', views.event_registration, name='event_registration'),
    path('participant_register', views.participant_registration, name='participant_registration'),
    path('event_dashboard', views.event_dashboard, name='event_dashboard'),
]