from django.urls import path,include
from .views import home_view,about_view,contact_view,program_view

urlpatterns = [
path('',home_view,name="home-page"),
path('about/',about_view,name="about-page"),
path('contact/',contact_view,name="contact-page"),
path('program/',program_view,name="program-page"),
]