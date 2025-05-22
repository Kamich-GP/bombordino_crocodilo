from django.contrib import admin
from .models import Category, Product, Cart


# Register your models here.
admin.site.register(Category) # Регистрируем категории
admin.site.register(Product) # Регистрируем товары
admin.site.register(Cart) # Регистрируем корзину
