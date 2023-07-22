from django.contrib import admin
<<<<<<< HEAD
from .models import Event, Ticket, Favorite

admin.site.register(Event)
admin.site.register(Ticket)
admin.site.register(Favorite)
=======
from .models import Event, Status
# Register your models here.
admin.site.register(Event)
admin.site.register(Status)
>>>>>>> 412f5edb1f16317d38d008c4e15d2479e221f630
