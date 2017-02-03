__author__ = 'dkoldyaev'

from django.contrib import admin
from django.db import models

from persons.models import Person

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'drinks_amount')

    def get_queryset(self, request):
        qs = super(PersonAdmin, self).get_queryset(request)
        qs = qs.annotate(models.Count('drinks'))
        return qs

    def drinks_amount(self, obj):
        return obj.drinks__count
    drinks_amount.admin_order_field = 'drinks__count'  

admin.site.register(Person, PersonAdmin)
