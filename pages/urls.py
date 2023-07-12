from django.urls import path
from .views import (HomePageView, AboutPageView, ContactPageView, 
                    TermsPageView, DevelopersPageView)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("contact/", ContactPageView.as_view(), name="contact"),
    path("terms/", TermsPageView.as_view(), name="terms"),
    path("developers/", DevelopersPageView.as_view(), name="developers"),
]
