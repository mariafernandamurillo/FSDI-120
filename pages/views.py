from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "pages/home.html"
    
class AboutPageView(TemplateView):
    template_name = "pages/about.html"

class ContactPageView(TemplateView):
    template_name = "pages/contact.html"

class TermsPageView(TemplateView):
    template_name = "pages/terms.html"

class DevelopersPageView(TemplateView):
    template_name = "pages/developers.html"