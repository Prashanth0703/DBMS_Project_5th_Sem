from django.urls import path
from . import views

app_name = 'doctor'
urlpatterns = [
    path('single-doctor-details/',views.DoctorDetails,name='singel-doctor-details'),
    path('single-nurse-details/',views.NurseDetails,name='singel-doctor-details'),
    path('',views.DetailChoices,name='home')
]