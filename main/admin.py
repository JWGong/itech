from django.contrib import admin
from .models import Category, Dish, Review


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    pass


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass
# Register your models here.
