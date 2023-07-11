from django.views.generic import ListView, DetailView, CreateView
from .models import Event
from .form import EventForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy



def detail(request):
    events = Event.object.all()
    context = {
        'events':events
    }
    return render(request, 'detail.html', context)

class EventListView(ListView):
    template_name = "events/list.html"
    model = Event

class EventDetailView(DetailView):
    template_name = "events/detail.html"
    model = Event

class EventCreateView(CreateView):
    template_name = "events/new.html"
    model = Event
    form_class = EventForm
    success_url = reverse_lazy("event_list")
