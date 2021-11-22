from django.shortcuts import render

# Create your views here.
from .models import Setting

def home(request):
    setting = Setting.objects.get(pk=1)
    context = {
        'setting':setting,
    }
    return render(request, 'index.html', context)

def contact_page(request):
    setting = Setting.objects.get(pk=1)
    context = {
        'setting':setting,
    }
    return render(request, 'pages/contactus.html', context)


def about_page(request):
    setting = Setting.objects.get(pk=1)
    context = {
        'setting':setting,
    }
    return render(request, 'pages/about.html', context)