from django.urls import path
from events import views

urlpatterns = [
    path("new/", views.EventCreateView.as_view(), name="create"),
    path("favorites/", views.EventFavoriteView.as_view(), name="favorites"),
    path("manager/", views.EventManagerView.as_view(), name="manager"),
    path("tickets_list/", views.TicketListView.as_view(), name="tickets_list"),
]