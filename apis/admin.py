from django.contrib import admin
from .models.user_models import Organization, CustomUser
from .models.event_models import Event, EventDetail, Participant, Certificate

# Register your models here.
admin.site.register(Organization)
admin.site.register(CustomUser)
admin.site.register(Event)
admin.site.register(EventDetail)
admin.site.register(Participant)
admin.site.register(Certificate)