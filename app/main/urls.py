from django.urls import path
from .views import *

urlpatterns = [
    path('', Main_view, name = 'main'),
    path('contact/', Contact_view, name = 'contact'),
    path('trainer/', Trainer_view, name = 'trainer'),
    path('why/', Why_view, name = 'why'),
]
