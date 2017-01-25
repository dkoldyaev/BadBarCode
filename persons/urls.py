__author__ = 'dkoldyaev'

from django.conf.urls import url

from persons.views import PersonListView, PersonRegisterView

urlpatterns = [
    url('^$', PersonListView.as_view(), name='rating'),
    url('^add', PersonRegisterView.as_view(), name='add_user'),
]