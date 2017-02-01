__author__ = 'dkoldyaev'

from django.views.generic import CreateView, ListView, View
from django.shortcuts import render
from django.urls import reverse

from persons.models import Person
from drinks.forms import DrinkForm



class PersonListView(ListView) :

    model = Person
    template_name = 'persons/rating.html'


class PersonRegisterView(CreateView) :

    model = Person
    fields = ['name', 'age', 'photo', 'status', 'barcode']
    template_name = 'persons/sign_in.html'
    success_url = '/person'