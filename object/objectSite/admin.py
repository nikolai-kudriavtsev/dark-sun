from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

admin.site.register(Type)
admin.site.register(Region)
admin.site.register(City)
admin.site.register(Sweets)
admin.site.register(Bank)
admin.site.register(Typerooms)
admin.site.register(Post)
admin.site.register(Worker)
admin.site.register(Object)
admin.site.register(Rooms)
admin.site.register(User, UserAdmin)
admin.site.register(Schedule)
admin.site.register(Dogovor)
admin.site.register(Settlement)
admin.site.register(Category)
admin.site.register(Service)
admin.site.register(Provide)
