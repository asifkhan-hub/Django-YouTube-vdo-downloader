from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('downloadmp3', views.downloadmp3, name="Downloadmp3"),
    path('downloadmp4', views.downloadmp4, name="Downloadmp4"),
    path('videodetails', views.videodetails, name="videodetails")
    
]