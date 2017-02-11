__author__ = 'dkoldyaev'

from django.contrib import admin
from django.db import models
from django.utils.safestring import mark_safe

from persons.models import Person

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'drinks_amount', 'image')
    fields = ('name', 'number', 'comment', 'banned')
    search_fields = ('number', 'name', 'id')

    def get_queryset(self, request):
        qs = super(PersonAdmin, self).get_queryset(request)
        qs = qs.annotate(models.Count('drinks'))
        return qs

    def drinks_amount(self, obj):
        return obj.drinks__count
    drinks_amount.admin_order_field = 'drinks__count'  

    def image(self, obj):
        try:
            return mark_safe('<img src="'+obj.photo+'" style="width:150px; height:auto;" />')
        except:
            return ''
        
admin.site.register(Person, PersonAdmin)
