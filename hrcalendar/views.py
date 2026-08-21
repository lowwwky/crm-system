from django.contrib import messages
from django.shortcuts import render, redirect

from candidates.models import HireCard
from hrcalendar.models import HRCalendar


# Create your views here.

def show_calendar(request):
    return render(request, 'hrcalendar/calendar.html')

def day_detail(request):
    ...

def event_detail(request, event_id):
    ...

def assign_new(request):
    ...

def delete_detail(request):
    ...

def delete_all(request):
    ...