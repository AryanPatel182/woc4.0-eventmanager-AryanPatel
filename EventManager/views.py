from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')    

def event_registration(request):
    return render(request, 'event_form.html')

def participant_registration(request):
    return render(request, 'participation_form.html')

def event_dashboard(request):
    return render(request, 'event_dashboard.html')