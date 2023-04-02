from django.contrib import admin
from django.utils.html import format_html
from .models import Stay, Photo, Suite, BookingInterval, AvailabilityCalendar, Booking, Payment

@admin.register(Stay)
class StayAdmin(admin.ModelAdmin):
    list_display = ('title', 'name', 'type', 'region', 'city',)
    list_filter = ('type', 'city',)
    search_fields = ('title', 'name', 'description',)
    filter_horizontal = ('photos',)


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'preview',)
    readonly_fields = ('preview',)

    def preview(self, obj):
        return format_html('<img src="{}" height="100" />'.format(obj.image.url))


@admin.register(Suite)
class SuiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'capacity',)
    list_filter = ('capacity',)

@admin.register(BookingInterval)
class BookingIntervalAdmin(admin.ModelAdmin):
    list_display = (
    'calendar',
    'check_in',
    'check_in_time',
    'check_out_time',
    'duration',
    'price',
    'available',
    )

@admin.register(AvailabilityCalendar)
class AvailabilityCalendarAdmin(admin.ModelAdmin):
    list_display = ('suite',)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'suite', 'total_price', 'confirmed',)
    list_filter = ('suite', 'confirmed',)
    search_fields = ('stay__title', 'stay__place_name', 'suite__name',)
    actions = ('confirm_bookings',)

    def confirm_bookings(self, request, queryset):
        updated = queryset.update(confirmed=True)
        self.message_user(request, f'{updated} booking(s) were confirmed.')
    confirm_bookings.short_description = 'Confirm selected bookings'


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'booking', 'payment_amount', 'payment_method', 'timestamp', 'successful',)
    list_filter = ('payment_method', 'timestamp', 'successful',)
    search_fields = ('booking__product__title', 'booking__product__place_name', 'booking__room_or_suite__name',)