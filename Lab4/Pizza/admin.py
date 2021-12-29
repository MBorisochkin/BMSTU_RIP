from django.contrib import admin

from .models import Pizza


class PizzaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        (None, {'fields': ['photo']}),
        ('Дополнительная информация', {'fields': ['topping', 'diameter'], 'classes': ['collapse']})
    ]

    search_fields = ['name']


admin.site.register(Pizza, PizzaAdmin)
