from typing import Any, Optional
from django.db import models
from django.db.models.query import QuerySet
from django.views.generic import (TemplateView,
                                  ListView,
                                  CreateView,
                                  DetailView, 
                                  UpdateView,
                                  DeleteView,
                                  View)
from django.contrib.auth.mixins import (
LoginRequiredMixin,
UserPassesTestMixin,
)
from .models import Event, Ticket, Favorite, Status, Profile, CATEGORY_CHOICES
from .form import EventForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy, reverse


def search_events(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        events =  Event.objects.filter(name__contains=searched)
        return render(request,'events/search_events.html',{'searched':searched,'events':events})
    else:
        return render(request,'events/search_events.html',{})
        

class ProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'account/my_account.html'
    model = Profile
    fields = '__all__'

    def get_object(self, queryset=None):
        user_id = self.kwargs.get("pk")
        profile = Profile.objects.get(user__id=user_id)
        return profile

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields.pop('user')
        return form

    def get_success_url(self):        
        return reverse('user',kwargs={'pk':self.object.user.id})

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



class EventCreateView(LoginRequiredMixin, CreateView):
    template_name = "events/new.html"
    model = Event
    form_class = EventForm

    def get_success_url(self):
        new_event = self.object
        status_name = new_event.status.name
        success_url = reverse_lazy(str(status_name))
        return success_url
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields.pop('organizer')
        return form

    def form_valid(self, form):
        form.instance.organizer = self.request.user
        return super().form_valid(form)

class CatListView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.kwargs.get('category')
        queryset = Event.objects.filter(category = category) 
        context["events_list"] = queryset        
        return context
    
    def get(self, request, *args, **kwargs):
        categories = self.get_context_data()
        categories["categories_list"] = CATEGORY_CHOICES
        return render(request, self.template_name, categories)
        
class EventDetailView(DetailView):
    template_name = "events/detail.html"
    model = Event

    def detail(request):
        events = Event.object.all()
        context = {
            'events':events
        }
        return render(request, 'detail.html', context)


class EventManagerView(TemplateView):
    template_name = "events/manager.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["events_list"] = Event.objects.all()        
        return context


class TicketListView(ListView):
    template_name = "tickets/list.html"
    model = Ticket

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tickets_list"] = Ticket.objects.all()
                
        return context


#CRUD VIEWS

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

class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'events/edit.html'
    model = Event
    form_class = EventForm
    success_url = reverse_lazy("published")

    def test_func(self):
        post = self.get_object()
        return post.organizer == self.request.user


class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'events/delete.html'
    model = Event
    success_url = reverse_lazy("published")

    def test_func(self):
        post = self.get_object()
        return post.organizer == self.request.user

#FAVORITE MODEL VIEWS 

class FavoriteView(View):
    model = Event

    def get(self, request):
        event = Event.objects.all()
        e_id = event.id

        if not e_id:
            return redirect('error-page')
        
        return HttpResponse("Hello!")
    

class EventFavoriteView(TemplateView):
    template_name = "events/favorites.html"


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


class EventListView(ListView):
    template_name = "events/list.html"
    model = Event

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        published_count = Event.objects.filter(status__name='published').count()
        context['published_count'] = published_count
        return context
    

