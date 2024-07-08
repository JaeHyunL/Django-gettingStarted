from django.contrib import admin

# Register your models here.
from .models import Question, Choice
from inventory.models import Car, Inventory

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Car)
admin.site.register(Inventory)
