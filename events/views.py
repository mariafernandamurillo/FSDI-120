from django.views.generic import (TemplateView,
                                  ListView,
                                  CreateView)

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Event, Ticket

class EventCreateView(LoginRequiredMixin, CreateView):
    template_name = "events/create.html"
    model = Event
    fields = ["name"]
    
class EventFavoriteView(TemplateView):
    template_name = "events/favorites.html"

class EventManagerView(TemplateView):
    template_name = "events/manager.html"

class TicketListView(ListView):
    template_name = "tickets/list.html"
    model = Ticket

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tickets_list"] = Ticket.objects.all()
                
        return context