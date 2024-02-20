from django.shortcuts import render
from events.models import *
from datetime import date
# Create your views here.
def index(requst):
    today=date.today()
    upcoming_event=Event.objects.filter(date__gte=today).order_by('date')[0]
    print("hell",upcoming_event)
    if upcoming_event:
        earliest_speech=Speech.objects.earliest('start_time')
        event_date=upcoming_event.date
        first_speech = Speech.objects.filter(event=upcoming_event).order_by('start_time').first()
        if first_speech:
            event_date_formatted=upcoming_event.date.strftime("%Y-%m-%d")
            event_time=first_speech.start_time.strftime( "%H:%M:%S" ) 
            print(event_date,event_time)
            contaxt={
                'event_date':event_date,
                'event_time':event_time,
                'event_date_formatted':event_date_formatted
            }
            return render(requst,'core/index.html',contaxt)
    return render(requst,'core/index.html',{})
# def user_profile(request):
#     return render(request,"core/user_profile.html")