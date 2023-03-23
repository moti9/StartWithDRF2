from django.db import models

# Create your models here.


class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class MenuItem(models.Model):
    title = models.SlugField()
    price = models.CharField(max_length=255)
    inventory = models.SmallIntegerField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)

    def __str__(self):
        return f"{self.title}-{self.price}"