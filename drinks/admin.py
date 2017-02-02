__author__ = 'dkoldyaev'

from django.contrib import admin
from django.db.models import Count

from drinks.models import Drink

class DrinkAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'person_drinks_count']
    def queryset(self, request, queryset):
        return queryset.annotate(person_drink_count=Count('person__drinks'))

admin.site.register(Drink)
