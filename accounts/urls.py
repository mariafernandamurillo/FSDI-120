#Add the paths to access the views
from django.urls import path
from accounts import views

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("my_account/", views.MyAccountView.as_view(), name="my_account"),
]