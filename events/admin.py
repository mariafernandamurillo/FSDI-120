from django.contrib import admin
from .models import Event, Ticket, Favorite

admin.site.register(Event)
admin.site.register(Ticket)
admin.site.register(Favorite)