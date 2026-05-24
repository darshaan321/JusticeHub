from django.contrib import admin
from .models import Lawyer
from .models import Client

admin.site.register(Lawyer)
admin.site.register(Client)


# Register your models here.
