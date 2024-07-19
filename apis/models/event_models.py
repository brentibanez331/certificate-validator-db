from django.db import models
from . import Organization, CustomUser

# Create your models here.
class EventDetail(models.Model):
    startDateTime = models.DateTimeField()
    endDateTime = models.DateTimeField()
    venue = models.CharField(max_length=255)
    description = models.TextField(null=True)

    def __str__(self):
        return f"{self.startDateTime} - {self.venue}"


class Event(models.Model):
    account = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    eventCertificate = models.ForeignKey('Certificate', on_delete=models.CASCADE)
    eventName = models.CharField(max_length=255)
    eventSubheading = models.CharField(max_length=255, null=True)
    eventDetail = models.ForeignKey(EventDetail, on_delete=models.CASCADE)

    def __str__(self):
        return self.eventName


class Participant(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=30, null=True)
    lastName = models.CharField(max_length=30, null=True)
    middleName = models.CharField(max_length=255, null=True)
    middleInitial = models.CharField(max_length=3, null=True)
    fullName = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"

class Certificate(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    eventCertificate = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='certificates')
    imagePath = models.CharField(max_length=255)
    qrCode = models.CharField(max_length=255)
    certificateExpirationDate = models.DateField(null=True)

    def __str__(self):
        return f"Certificate for {self.participant}"