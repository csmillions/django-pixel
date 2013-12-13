from django.contrib import admin
from django_pixel.models import Pixel

class PixelAdmin(admin.ModelAdmin):
	pass


admin.site.register(Pixel, PixelAdmin)
