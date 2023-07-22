<<<<<<< HEAD
#Add the paths to access the views
=======
>>>>>>> 412f5edb1f16317d38d008c4e15d2479e221f630
from django.urls import path
from accounts import views

urlpatterns = [
<<<<<<< HEAD
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("my_account/", views.MyAccountView.as_view(), name="my_account"),
=======
    path('signup/',views.SignUpView.as_view(), name='signup' ),
>>>>>>> 412f5edb1f16317d38d008c4e15d2479e221f630
]