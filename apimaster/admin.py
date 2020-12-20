from django.contrib import admin

from .models import *

admin.site.register(pizzaModel)
admin.site.register(pizzaTopping)
admin.site.register(pizzaSize)
admin.site.register(typeOfPizza)

