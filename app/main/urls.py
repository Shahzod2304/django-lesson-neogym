from django.urls import path
from .views import *

urlpatterns = [
    path('', Main, name = 'main'),
    path('contact/', Contact, name = 'contact'),
    path('trainer/', Trainer, name = 'trainer'),
    path('why/', Why, name = 'why'),
]
