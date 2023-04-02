from django.contrib import admin
from .models import Category, Service, ServiceOption, StayService

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(ServiceOption)
class ServiceOptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'price',)


class ServiceOptionInline(admin.TabularInline):
    model = StayService.options.through


@admin.register(StayService)
class StayServiceAdmin(admin.ModelAdmin):
    list_display = ('stay', 'service',)
    list_filter = ('stay', 'service',)
    search_fields = ('product__title', 'product__place_name', 'service__name',)
    inlines = [ServiceOptionInline]
