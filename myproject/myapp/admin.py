from django.contrib import admin

# Register your models here.
# Import the models from models.py

# Register your models here.
from .models import Booking, DrinksCategory, Drinks

admin.site.register(Drinks)

admin.site.register(DrinksCategory)


admin.site.register(Booking)