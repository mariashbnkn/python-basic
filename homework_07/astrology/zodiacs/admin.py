from django.contrib import admin

from .models import Zodiacs, ZodiacBase


@admin.register(Zodiacs)
class ZodiacsAdmin(admin.ModelAdmin):
    list_display = "id", "name"
    list_display_links = "id", "name"


@admin.register(ZodiacBase)
class CategoryAdmin(admin.ModelAdmin):
    list_display = "id", "name"
    list_display_links = "id", "name"
