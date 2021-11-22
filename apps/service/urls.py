from django.urls import path
from apps.service.views import service_page

urlpatterns = [
    path('', service_page, name="service"),
]