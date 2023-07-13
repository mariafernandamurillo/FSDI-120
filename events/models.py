from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from location_field.models.plain import PlainLocationField
from django.utils import timezone

CATEGORY_CHOICES = [
    ('Arts', 'Arts'),
    ('Music', 'Music'),
    ('Health', 'Health'),
    ('Games', 'Games'),
    ('Sports', 'Sports'),
    ('Technology', 'Technology'),
    ('Support', 'Support'),
]

MODALITY_CHOICES = [
    ('Online', 'Online'),
    ('In-person', 'In-person'),
]

CITY_CHOICES = [
    ('Los Angeles', 'Los Angeles'),
    ('San Francisco', 'San Francisco'),
    ('San Diego', 'San Diego'),
    ('Sacramento', 'Sacramento'),
    ('San Jose', 'San Jose'),
    ('Oakland', 'Oakland'),
    ('Long Beach', 'Long Beach'),
    ('Fresno', 'Fresno'),
    ('Bakersfield', 'Bakersfield'),
    ('Santa Ana', 'Santa Ana'),
    # Add more cities here
]

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=128) 
    description = models.TextField()
    date = models.DateField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    organizer = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    category = models.CharField(max_length=128, choices=CATEGORY_CHOICES, default='Arts')
    modality = models.CharField(max_length=128, choices=MODALITY_CHOICES, default='Virtual')
    city = models.CharField(max_length=128, choices=CITY_CHOICES, default='San Diego')
    location = PlainLocationField(based_fields=['city'], zoom=7, null=True, blank=True)

    def __str__(self):
        return self.name
    
class Ticket(models.Model):
    join_date = models.DateTimeField(default=timezone.now)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    #def __str__(self):
        #return self.name
    

#Attributes of Event Model

#Name
#Description
#Time: At 10:00 a.m.

#Duration: n hours ()

#Location -> Research -> Place or Online
#Category -> Research

#Organizer

#Date -> Research
#Image -> Research

#On site - Virtual

#EVENT 
# Delete -> Aaron
# Edit -> Aaron

#USER MODEL
#Name
#Email
#Password
#Picture - Optional - A tag or icon by default -> Reseatch Fer. 


#TICKET MODEL
#Even name
#Event date
#Event image
#Subscription day 
#Event details