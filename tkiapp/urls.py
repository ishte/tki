
from django.urls import path
from .views import *
urlpatterns = [
    path('register/',RegistrationView.as_view()),          
    path('login/',LoginView.as_view()),
    path('logout/',LogOutView.as_view()),
    path('PaymentInstallment/',PaymentInstallmentView.as_view() ),
    path('projecttracker/',ProjectTrackerView.as_view() ),
    path('projecdetail/',ProjectDetailView.as_view() ),
    path('team/',TeamNameView.as_view() ),
 
]
