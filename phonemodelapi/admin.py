from django.contrib import admin
from .models import PhoneImage, Brand, Color, OperatingSystem, OSVersion, Chipset, QuickCharge, Phone, Rating

admin.site.register(PhoneImage)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(OperatingSystem)
admin.site.register(OSVersion)
admin.site.register(Chipset)
admin.site.register(QuickCharge)
admin.site.register(Phone)
admin.site.register(Rating)
