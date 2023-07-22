from django.urls import path
from events import views

urlpatterns = [
    path("new/", views.EventCreateView.as_view(), name="create"),
    #path("favorites/", views.EventFavoriteView.as_view(), name="favorites"),
    path("manager/", views.EventManagerView.as_view(), name="manager"),
    path("tickets_list/", views.TicketListView.as_view(), name="tickets_list"),
    path("<int:pk>/", views.EventDetailView.as_view(), name="event_detail"),
    path("favorites_list/", views.FavoriteListView.as_view(), name="favorites_list"),
    path("add_favorite/", views.FavoriteAddView.as_view(), name="add_favorite"),
    path("probando/", views.SimpleView.as_view(), name="probando"),
    path('fav/', views.FavoriteView.as_view(), name='fav'),
    path('error-page/', views.ErrorPageView.as_view(), name='error-page'),  # Add the URL pattern for the error page
]