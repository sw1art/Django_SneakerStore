from django.contrib import admin

from .models import Sneaker, Size, Brand

class SneakerAdmin(admin.ModelAdmin):
    list_display = ('title', 'brand', 'price', 'image')
    search_fields = ('title', 'brand')
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Sneaker, SneakerAdmin)
admin.site.register(Size)
admin.site.register(Brand)
