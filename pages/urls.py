from django.urls import path
<<<<<<< HEAD
from .views import (HomePageView, AboutPageView, ContactPageView, 
                    TermsPageView, DevelopersPageView)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("contact/", ContactPageView.as_view(), name="contact"),
    path("terms/", TermsPageView.as_view(), name="terms"),
    path("developers/", DevelopersPageView.as_view(), name="developers"),
] 
=======
from .views import HomePageView, AboutPageView

urlpatterns = [
    path("",HomePageView.as_view(),name="home"),
    path("about/",AboutPageView.as_view(),name="about"),
]
>>>>>>> 412f5edb1f16317d38d008c4e15d2479e221f630
