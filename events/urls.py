from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import ( 
    EventListView,
    EventDetailView,
    EventCreateView,
)

urlpatterns = [
    path("",EventListView.as_view(), name="event_list"),
    path("<int:pk>/", EventDetailView.as_view(), name="event_detail"),
    path("new/", EventCreateView.as_view(), name="event_new"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)