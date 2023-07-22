from django.views.generic import TemplateView
<<<<<<< HEAD
from events.models import Event, CATEGORY_CHOICES
from django.shortcuts import render


class HomePageView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["events_list"] = Event.objects.all()        
        return context
    
    def get(self, request, *args, **kwargs):
        categories = self.get_context_data()
        categories["categories_list"] = CATEGORY_CHOICES
        return render(request, self.template_name, categories)

class AboutPageView(TemplateView):
    template_name = "pages/about.html"
    
class ContactPageView(TemplateView):
    template_name = "pages/contact.html"

class TermsPageView(TemplateView):
    template_name = "pages/terms.html"

class DevelopersPageView(TemplateView):
    template_name = "pages/developers.html"
=======

class HomePageView(TemplateView):
    template_name = "pages/home.html"

class AboutPageView(TemplateView):
    template_name = "pages/about.html"
>>>>>>> 412f5edb1f16317d38d008c4e15d2479e221f630
