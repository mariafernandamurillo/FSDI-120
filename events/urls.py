from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from events import views

urlpatterns = [
    path("", views.EventListView.as_view(), name="published"),
    path("<int:pk>/", views.EventDetailView.as_view(), name="event_detail"),
    path("new/", views.EventCreateView.as_view(), name="event_new"),
    path("archived/", views.ArchiveEventListView.as_view(), name="archived"),
    path('drafts/', views.DraftEventListView.as_view(), name="draft"),
    path("<int:pk>/edit/", views.EventUpdateView.as_view(), name="event_edit"),
    path("<int:pk>/delete/", views.EventDeleteView.as_view(), name="event_delete"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)