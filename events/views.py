<<<<<<< HEAD
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
=======
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Event, Status
from .form import EventForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse

from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)

class EventListView(ListView):
    template_name = "events/list.html"
    model = Event

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        published_count = Event.objects.filter(status__name='published').count()
        context['published_count'] = published_count
        return context


class DraftEventListView(LoginRequiredMixin, ListView):
    template_name = "events/draft.html"
    model = Event
    context_object_name = 'event_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        draft_count = Event.objects.filter(status__name='draft').count()
        context['draft_count'] = draft_count
        return context


class ArchiveEventListView(LoginRequiredMixin, ListView):
    template_name = "events/archived.html"
    model = Event

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        archived_count = Event.objects.filter(status__name='archvied').count()
        context['archived_count'] = archived_count
        return context


class EventDetailView(DetailView):
    template_name = "events/detail.html"
    model = Event

    def detail(request):
        events = Event.object.all()
        context = {
            'events':events
        }
        return render(request, 'detail.html', context)


class EventCreateView(LoginRequiredMixin, CreateView):
    template_name = "events/new.html"
    model = Event
    form_class = EventForm

    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     draft_status = Status.objects.get(name= 'draft')
    #     form.instance.status = draft_status
    #     return super().form_valid(form)
    
    def get_success_url(self):
        new_event = self.object
        status_name = new_event.status.name
        success_url = reverse_lazy(str(status_name))
        return success_url

class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'events/edit.html'
    model = Event
    form_class = EventForm
    success_url = reverse_lazy("published")

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user


class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'events/delete.html'
    model = Event
    success_url = reverse_lazy("published")

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user


>>>>>>> 412f5edb1f16317d38d008c4e15d2479e221f630
