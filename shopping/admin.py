from django.contrib import admin
from .models import Category, Product, ProductImage, Variant

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'parent')
    prepopulated_fields = { 'slug': ('name',) }


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class VariantInline(admin.TabularInline):
    model = Variant
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'category', 'brand', 'price', 'is_active')
    prepopulated_fields = { 'slug': ('title',) }
    inlines = [ProductImageInline, VariantInline]