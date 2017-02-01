__author__ = 'dkoldyaev'

from django.conf.urls import url

from drinks.views import DrinkView

urlpatterns = [
    url('^$', DrinkView.as_view(), name='drink'),
]