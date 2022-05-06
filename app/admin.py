from django.contrib import admin
from .models import Pizza,PizzaCategory,Cart,CardItems
# Register your models here.

admin.site.register(Pizza)
admin.site.register(PizzaCategory)
admin.site.register(Cart)
admin.site.register(CardItems)