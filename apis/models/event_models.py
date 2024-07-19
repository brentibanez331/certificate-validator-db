from django.db import models

# Create your models here.
class EventDetail(models.Model):
    startDateTime = models.DateTimeField()
    endDateTime = models.DateTimeField()
    venue = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.startDateTime} - {self.venue}"


# class Event(models.Model):
#     account =
