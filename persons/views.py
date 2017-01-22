__author__ = 'dkoldyaev'

from django.views.generic import CreateView, ListView, View
from django.shortcuts import render

from persons.models import Person
from drinks.forms import DrinkForm


class PersonRegisterView(CreateView) :

    model = Person
    template_name = 'persons/sign_in.html'

class PersonListView(ListView) :

    model = Person
    template_name = ''