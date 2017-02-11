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
        message = None
        try:
            if code :
                person = Person.objects.get(number=code)
            else :
                person = None 
                pass #person = None
        except : #Person.DoesNotExist:
            person = None
            with open('fucking-code.log', 'w') as log:
                log.write(code+'\n')
            #return redirect('/person/add')

        if code and person and not person.banned:
            try: 
                drink = Drink(person=person)
                drink.save()
            except:
                pass
        elif person and person.banned :
            message = 'Забанен!!11'

        last_persons = Person.objects.all().order_by('-drinks__date')[:3]

        return render(
            request,
            'drinks/go.html',
            {
                'code': code,
                'person': person,
                # 'last_persons': Person.objects.all().order_by('-date_create')[:3]
                'last_persons': last_persons
            }
        )
