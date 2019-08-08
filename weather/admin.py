from django.contrib import admin
from weather.models import City

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['name']