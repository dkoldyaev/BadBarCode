__author__ = 'dkoldyaev'

from django.views.generic import CreateView, ListView, View
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.core import serializers

from drinks.models import Drink
from persons.models import Person


class DrinkView(View) :

    def get(self, request):
        code = request.GET.get('code', False)
        try:
            if code :
                person = Person.objects.get(number=code)
            else :
                person = None
        except Person.DoesNotExist:
            return redirect('/person/add')

        if code :
            drink = Drink(person=person)
            drink.save()

        return render(
            request,
            'drinks/go.html',
            {
                'code': code,
                'person': person,
                'last_persons': Person.objects.all().order_by('-date_create')[:3]
            }
        )
