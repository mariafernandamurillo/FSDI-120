from django.views.generic import (TemplateView,
                                  ListView,
                                  CreateView,
                                  DetailView, 
                                  View)

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Event, Ticket, Favorite

from django.http import HttpResponse

from django.shortcuts import render, redirect

class EventCreateView(LoginRequiredMixin, CreateView):
    template_name = "events/create.html"
    model = Event
    fields = ["name", "status"]

class EventDetailView(DetailView):
    template_name = "events/detail.html"
    model = Event
    
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

#FAVORITE MODEL VIEWS 

class FavoriteView(View):
    model = Event

    def get(self, request):
        event = Event.objects.all()
        e_id = event.id

        if not e_id:
            return redirect('error-page')
        
        return HttpResponse("Hello!")

class ErrorPageView(View):
    def get(self, request):
        return HttpResponse("Error: event_pk is not provided.")  # Return an error message as the response
    
class FavoriteAddView(LoginRequiredMixin, CreateView):
    template_name = "favorites/add_favorite.html"
    model = Favorite
    fields = ["join_date", "status", "_id"]

class FavoriteListView(ListView):
    template_name = "favorites/list.html"
    model = Favorite

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["favorites_list"] = Favorite.objects.all()
                
        return context
    
class SimpleView(View):
    def get(self, request):
        # This view returns a plain text response
        return HttpResponse("Hello, this is a simple view!")