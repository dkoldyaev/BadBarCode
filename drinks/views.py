__author__ = 'dkoldyaev'

from django.views.generic import CreateView, ListView, View
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers

from drinks.models import Drink
from persons.models import Person

class DrinkView2(ListView):

    model = Person
    page_size = 3
    template_name='drinks/go.html'

    def get_context_data(self, request):
        context = super(DrinkViews, self).get_context_data(request)
        try:
            code = request.GET.get('code')
            context['new_user'] = Person.objects.get(number=code)
        except:
            pass

        


class DrinkView(View) :

    template_name = 'drinks/go.html'

    def get(self, request):
        context = super(DrinkView, self).get_context_data(request)
        achievement = []
        person = None
        errors = []
        last_person = Person.objects.all().order_by('-date_create')[0]
        last_persons = Person.objects.all().order_by('-date_create')[1:4]
        if request.GET.get('person_id', False) :
            try :
                person = Person.objects.get(id=request.GET.get('person_id'))
            except Person.DoesNotExist :
                pass
            new_drink = Drink()
            new_drink.person = person
            new_drink.save()
        context['person'] = person
        context['drink'] = drink

        return HttpResponse()

        return context


        return JsonResponse({
            'person':       person,
            'achievement':  achievement
        })

        
