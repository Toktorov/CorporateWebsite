from django.shortcuts import render

# Create your views here.
from apps.home.models import Setting

# Create your views here.

def service_page(request):
    setting = Setting.objects.get(pk=1)
    context = {
        'setting':setting,
    }
    return render(request, 'pages/service.html', context)