from django.contrib import admin
from .models import PhoneImage, Brand, OperatingSystem, Phone, Rating

admin.site.register(PhoneImage)
admin.site.register(Brand)
admin.site.register(OperatingSystem)
admin.site.register(Phone)
admin.site.register(Rating)
