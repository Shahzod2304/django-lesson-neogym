from urllib import request
from django.shortcuts import render
from .models import *

# Create your views here.
def Main(request):
    context = {
        'home_data' : Home.objects.all(),
        'why_data' : Why.objects.all().order_by('-id')[:4],
    
        'home_content_data' : HomeContent.objects.last(),
        'active_page' : 'main',
       
    }
    print(Why.objects.all()[0:3].values())
    return render(request, 'index.html', context)

def Contact(request):
    context = {
        'active_page':'contact',
    }

    return render(request, 'contact.html', context)

def Trainer(request):
    context = {
        'active_page':'trainer',
    }

    return render(request, 'trainer.html', context)

def Why_view(request):
    context = {
        'active_page':'why',
    }

    return render(request, 'why.html', context)