from django.db import models


class Sneaker(models.Model):
    title = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    description = models.TextField(max_length=400)
    price = models.DecimalField(max_digits=7)
    release_date = models.DateField()
    sizes = models.ManyToManyField('Size')
    # image = models.ImageField()

    def __str__(self):
        return self.name


class Size(models.Model):
    size_us = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)
    size_ru = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)
    size_uk = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)
    size_cm = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)

    def __str__(self):
        return f"US: {self.size_us}, RU: {self.size_ru}, UK: {self.size_uk}, CM: {self.size_cm}"