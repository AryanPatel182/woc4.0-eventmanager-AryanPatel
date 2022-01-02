from django.http.response import HttpResponse
from django.shortcuts import render

from EventManager.models import Event, Participant

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
        event.save()

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
        evnt = Event.objects.get(name=event_name)   

        participant = Participant(participant_name=participant_name, contact_no=contact_no, participant_email=participant_email, event_name=evnt, registration_type=registration_type, no_of_people=no_of_people)

        participant.save()
        # print(participant)
        return render(request, 'index.html')

    context = {'event_list': Event.objects.all()}
    return render(request, 'participation_form.html', context)

def event_dashboard(request):
    return render(request, 'event_dashboard.html')

