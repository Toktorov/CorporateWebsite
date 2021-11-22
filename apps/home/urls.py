from django.urls import path
from apps.home.views import home, contact_page,about_page

urlpatterns = [
    path('', home, name="home"),
    path('contact-us/', contact_page, name="contact"),
    path('about-us/', about_page, name="about"),
]