#register the tables who can admin see
from django.contrib import admin
from .models import Drink

admin.site.register(Drink)

