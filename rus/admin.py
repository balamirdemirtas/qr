from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Category,Product,BestOfWeek
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','parent','name','slug']
    prepopulated_fields = {'slug':('name',)}
    class Meta:
        model = Category




@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','slug','category','price','available','created']
    list_editable = ['price','available']
    prepopulated_fields = {'slug':('name',)}

    class Meta:
        model = Product



@admin.register(BestOfWeek)
class BestofWeekAdmin(admin.ModelAdmin):
    list_display = ['id', 'slug', 'name', 'slug','price']
    prepopulated_fields = {'slug': ('name',)}

    class Meta:
        model = BestOfWeek



