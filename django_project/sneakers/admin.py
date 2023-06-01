from django.contrib import admin

from .models import Sneaker, Size, Brand, Review

class RewiewInline(admin.TabularInline):
    model = Review

class SneakerAdmin(admin.ModelAdmin):
    inlines = [RewiewInline]
    list_display = ('title', 'brand', 'price', 'image')
    search_fields = ('title', 'brand')
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Sneaker, SneakerAdmin)
admin.site.register(Size)
admin.site.register(Brand)
