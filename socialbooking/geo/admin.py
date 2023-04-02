from django.contrib import admin
from .models import City, Region, Coordinates, Address

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'region',)
    list_filter = ('region',)


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Coordinates)
class CoordinatesAdmin(admin.ModelAdmin):
    list_display = ('latitude', 'longitude',)

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('city', 'street', 'house_number', 'building_number', 'apartment_number', 'postal_code')
    list_filter = ('city',)
    search_fields = ('city__name', 'street', 'house_number', 'building_number', 'apartment_number', 'postal_code')
