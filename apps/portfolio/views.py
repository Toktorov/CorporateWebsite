from django.shortcuts import render
from apps.home.models import Setting

# Create your views here.

def portfolio_page(request):
    setting = Setting.objects.get(pk=1)
    context = {
        'setting':setting,
    }
    return render(request, 'pages/portfolio.html', context)