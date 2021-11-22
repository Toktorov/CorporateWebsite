from django.urls import path
from apps.portfolio.views import portfolio_page

urlpatterns = [
    path('portfolio/', portfolio_page, name="portfolio"),
]