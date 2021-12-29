from django.contrib import admin

from .models import Driver, Carstation


class DriverAdmin(admin.ModelAdmin):
    fields = ['second_name', 'first_name', 'salary', 'carstation_id']
    search_fields = ['second_name', 'first_name']


class CarstationAdmin(admin.ModelAdmin):
    fields = ['name', 'adress']
    search_fields = ['name']


admin.site.register(Driver, DriverAdmin)
admin.site.register(Carstation, CarstationAdmin)
