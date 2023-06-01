from django.db import models
from django.urls import reverse
from django.utils.text import slugify

import uuid

class Brand(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=400, null=True, blank=True)
    logo = models.ImageField(upload_to='brand_logos/', null=True, blank=True)

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return self.name

class Sneaker(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(unique=True, max_length=300)
    brand = models.ForeignKey(to=Brand, on_delete=models.CASCADE)
    description = models.TextField(max_length=2000, null=True, blank=True)
    feature = models.TextField(max_length=500, null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=0)
    release_date = models.DateField(null=True, blank=True)
    sizes = models.ManyToManyField('Size')
    image = models.ImageField(upload_to='sneaker_images/', default='sneaker_images/default.jpg')
    slug = models.SlugField(null=False, unique=True, max_length=310)

    class Meta:
        verbose_name = 'Кроссовки'
        verbose_name_plural = 'Кроссовки'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f'{slugify(self.title)}{self.id}'
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('sneaker_detail', kwargs={"slug": self.slug, "uuid": self.id})
    
    def __str__(self):
        return self.title
    

class Size(models.Model):
    size_us = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    size_ru = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    size_eu = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    size_uk = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    size_cm = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'

    def __str__(self):
        return f"US: {self.size_us}, RU: {self.size_ru}, UK: {self.size_uk}, CM: {self.size_cm}"
    