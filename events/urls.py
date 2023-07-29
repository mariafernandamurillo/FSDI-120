from django.urls import path
from events import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("my_account/<int:pk>/", views.ProfileView.as_view(), name="user"),
    path("new/", views.EventCreateView.as_view(), name="create"),
    path("search_events/", views.search_events, name="search_events"),
    # CRUD
    path("archived/", views.ArchiveEventListView.as_view(), name="archived"),
    path('drafts/', views.DraftEventListView.as_view(), name="draft"),
    path("<int:pk>/edit/", views.EventUpdateView.as_view(), name="event_edit"),
    path("<int:pk>/delete/", views.EventDeleteView.as_view(),name="event_delete"), 
    path("", views.EventListView.as_view(), name="published"),
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

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
