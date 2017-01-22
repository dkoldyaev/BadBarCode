__author__ = 'dkoldyaev'

from django.contrib import admin

from persons.models import Person

admin.site.register(Person)