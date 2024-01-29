from urllib import request
from django.shortcuts import render
from .models import *

# Create your views here.
def Main_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, phone_number=phone_number,message=message)
        contact.save()

    context = {
        'home_data' : Home.objects.all(),
        'why_data' : Why.objects.all().order_by('-id')[:4],
        'trainer': Trainer.objects.all(),
        'home_content_data' : HomeContent.objects.last(),
        'footer_data' : Footer.objects.last(),
        'active_page' : 'main',       
    }
    
    return render(request, 'index.html', context)

def Contact_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, phone_number=phone_number,message=message)
        contact.save()
        
    context = {
        'active_page':'contact',
        'footer_data' : Footer.objects.last(),

    }

    return render(request, 'contact.html', context)

def Trainer_view(request):
    context = {
        'active_page':'trainer',
        'trainer': Trainer.objects.all(),
        'footer_data' : Footer.objects.last(),
    }

    return render(request, 'trainer.html', context)

def Why_view(request):
    context = {
        'active_page':'why',
        'why_data' : Why.objects.all().order_by('-id')[:4],
        'footer_data' : Footer.objects.last(),
    }

    return render(request, 'why.html', context)