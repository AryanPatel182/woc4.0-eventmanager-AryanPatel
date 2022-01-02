from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=30)
    desc = models.CharField(max_length=200)
    poster_link = models.URLField( max_length=200)
    from_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    to_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    deadline = models.DateTimeField(auto_now=False, auto_now_add=False)
    host_email = models.EmailField(max_length=254)
    password = models.CharField(max_length=32, default="")

class Participant(models.Model):
    participant_name = models.CharField(max_length=30,default="")
    contact_no = models.BigIntegerField()    
    participant_email = models.EmailField(max_length=254)
    event_name = models.ForeignKey(Event, on_delete=models.CASCADE)
    registration_type = models.CharField(max_length=20)
    no_of_people = models.IntegerField(default=1)