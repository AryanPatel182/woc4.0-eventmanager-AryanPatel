from django.core.checks import messages
from django.http.response import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from EventManager.models import Event, Participant
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()
# Create your views here.
def index(request):
    return render(request, 'index.html')    

def event_registration(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        poster_link = request.POST.get('poster_link')
        from_date = request.POST.get('from_date')
        to_date = request.POST.get('to_date')
        deadline = request.POST.get('deadline')
        host_email = request.POST.get('host_email')
        password = request.POST.get('password')

        event = Event(name=name, desc=desc, poster_link=poster_link, from_date=from_date, to_date=to_date, deadline=deadline, host_email=host_email, password=password)        
        # event.save()
        send_mail(
           'Your event :',
            'Here is the confirmation message.\n Good Luck !',
            os.environ.get("EMAIL_HOST_USER"),
            [host_email],
            fail_silently=False,
        )
        return render(request, 'index.html')
    return render(request, 'event_form.html')

def participant_registration(request):
    if request.method == 'POST':
        participant_name = request.POST.get('participant_name')
        contact_no = request.POST.get('contact_no')
        participant_email = request.POST.get('participant_email')
        event_name = request.POST.get('event_name')
        registration_type = request.POST.get('registration_type')
        no_of_people = request.POST.get('no_of_people')    
        evnt = Event.objects.all().filter(name=event_name).first()   

        # Already Registered
        if Participant.objects.all().filter(participant_name=participant_name, contact_no=contact_no,participant_email=participant_email,event_name=evnt):
            context = {'event_list': Event.objects.all().filter(deadline__gte=datetime.now()) ,'messages':"You have already participated in the event !"}
            return render(request, 'participation_form.html', context)

        # New participant
        participant = Participant(participant_name=participant_name, contact_no=contact_no, participant_email=participant_email, event_name=evnt, registration_type=registration_type, no_of_people=no_of_people)

        # participant.save()
        # print(participant)        

    context = {'event_list': Event.objects.all().filter(deadline__gte=datetime.now())}
    return render(request, 'participation_form.html', context)

def event_dashboard(request):
    if request.method == 'POST':
        event_id = request.POST.get('event_id')
        password = request.POST.get('password')

        
        if  Event.objects.all().filter(id=event_id).exists() and Event.objects.get(id=event_id).password == password:
            context = {'participant_list': Participant.objects.all().filter(event_name=event_id)}
            return render(request, 'event_dashboard.html',context) 
        else:
            context = {'messages':"Username or password is incorrect !"}
            return render(request, 'event_dashboard.html', context)
    return render(request, 'event_dashboard.html')

