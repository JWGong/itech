from django.db import models
from django.contrib.auth import settings
from datetime import datetime


class Category(models.Model):
    name = models.CharField(max_length=1024)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"


class Dish(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=1024)
    description = models.CharField(max_length=1024)
    rating = models.FloatField()
    img = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Dish"


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    comments = models.TextField()
    addTime = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.comments

    class Meta:
        verbose_name = "Review"
