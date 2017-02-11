__author__ = 'dkoldyaev'

from django.contrib import admin
from django.db.models import Count
from django.http import HttpResponse

from drinks.models import Drink

def export_to_csv(modeladmin, request, queryset):
    import csv, os, io, datetime
    from django.conf import settings
    export_file = os.path.join(settings.BASE_DIR, '..', 'export')
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="drinks_list_%s.csv"' % datetime.datetime.now().__str__()
    writer = csv.DictWriter(
        response,
        dialect='excel',
        fieldnames=(
            'person_first',#:     'Первокурсник',
            'person_id',#:        'ID',
            'person__name',#:     'Имя',
            'person__number',#:   'Номер',
            'person__comment',#:  'Смешной коммент',
            'person__banned',#:   'Забанен',
            'date',#:             'Дата дринка'
        )
    )

    writer.writeheader()

    data = queryset.values(
        'person_id',
        'person__name',
        'person__number',
        'person__comment',
        'person__banned',
        'date')

    for drink_data in data :
        pekus = 'первокурсник' if len(drink_data['person__number']) < 5 else ' '
        if drink_data['person__banned'] :
            drink_data['person__banned'] = 'Забанен'
        else:
            drink_data['person__banned'] = ''
        drink_data.update({
            'person_first':pekus
        })

    writer.writerows(data)
    return response

export_to_csv.short_description = "Экспорт в csv"

class DrinkAdmin(admin.ModelAdmin):
    list_display = ['person', 'date',]
    actions = [export_to_csv]

admin.site.register(Drink, DrinkAdmin)
