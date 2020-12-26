from django.urls import path
from . import views

app_name = 'patient'
urlpatterns = [
    path('single-patient-details/',views.PatientDetails,name='singel-patient-details'),
    path('',views.DetailChoices,name='home')
]