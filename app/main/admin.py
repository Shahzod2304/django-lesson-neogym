from django.contrib import admin

from main.models import Home
from .models import *

admin.site.register(Home)
admin.site.register(Why)
admin.site.register(HomeContent)
admin.site.register(Trainer)
admin.site.register(Footer)
admin.site.register(Contact)

# Register your models here.
