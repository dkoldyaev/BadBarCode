__author__ = 'dkoldyaev'

from django import forms
from django.forms import fields

class DrinkForm(forms.Form) :

    person =     fields.IntegerField(required=True)

    def clean_person_id(self):
        person_id = self.cleaned_data['person']
        from persons.models import Person
        try:
            return Person.objects.get(id=person_id)
        except Person.DoesNotExist as e :
            raise forms.ValidationError('Нужно зарегистрироваться')