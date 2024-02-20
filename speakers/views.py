from django.shortcuts import render
from .models import NationalSpeaker,InterNationalSpeaker
# Create your views here.
def Spekaers(request):
    n_speakers=NationalSpeaker.objects.all()
    I_speakers=InterNationalSpeaker.objects.all()
    context={
        'n_speakers':n_speakers,
        'I_speakers':I_speakers
    }
    return render(request,'core/speakers.html',context)