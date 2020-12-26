from django.urls import path
from . import views

app_name = 'ward'
urlpatterns = [
    path('single-ward-details/',views.WardDetails,name='singel-ward-details'),
    path('',views.DetailChoices,name='home')
]