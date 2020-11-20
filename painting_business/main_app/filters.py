import django_filters

from .models import painting_information
from django.db import models

class PaintFilter(django_filters.FilterSet):
    class Meta:
        model = painting_information
        fields ='__all__'
        exclude = ['slug', 'photo', 'painting_id']
        filter_overrides = {
            models.ImageField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'exact',
                },
            },
        }




