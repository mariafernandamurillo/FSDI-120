from django.contrib import admin
from .models import Event, Ticket, Favorite, Status, Profile

admin.site.register(Event)
admin.site.register(Ticket)
admin.site.register(Favorite)
admin.site.register(Status)
admin.site.register(Profile)
