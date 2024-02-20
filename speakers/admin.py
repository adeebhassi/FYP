from django.contrib import admin
from .models import NationalSpeaker, InterNationalSpeaker
from django.http import HttpResponse
import csv

class BaseSpeakersAdmin(admin.ModelAdmin):
    list_display = ['name', 'designation', 'image']

    def generate_speakers_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="speakers.csv"'

        writer = csv.writer(response)
        writer.writerow(['Name', 'Image', 'Designation', 'Speaker Type'])

        for speaker in queryset:
            if isinstance(speaker, NationalSpeaker):
                speaker_type = 'National'
                image_url = str(speaker.image)
            elif isinstance(speaker, InterNationalSpeaker):
                speaker_type = 'International'
                image_url = str(speaker.image)
            else:
                speaker_type = 'Unknown'
                image_url = ''

            writer.writerow([speaker.name, image_url, speaker.designation, speaker_type])

        return response

    generate_speakers_csv.short_description = 'Generate CSV for selected speakers'

class NationalSpeakersAdmin(BaseSpeakersAdmin):
    actions = ['generate_speakers_csv']

class InternationSpeakersAdmin(BaseSpeakersAdmin):
    actions = ['generate_speakers_csv']

    def generate_speakers_csv(self, request, queryset):
        return super().generate_speakers_csv(request, queryset)

admin.site.register(NationalSpeaker, NationalSpeakersAdmin)
admin.site.register(InterNationalSpeaker, InternationSpeakersAdmin)
