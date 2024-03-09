import django_filters
from django_filters import DateFilter, CharFilter
from django import forms
from datetime import datetime

from .models import *

class OrderFilter(django_filters.FilterSet):
    date_field1 = django_filters.DateFilter(field_name="date_created", label='Date greater than', lookup_expr='gte', widget=forms.DateInput(attrs={'type':'date'}))
    date_field = django_filters.DateFilter(field_name="date_created", label='Date less than', lookup_expr='lte', widget=forms.DateInput(attrs={'type':'date', 'max': datetime.now().date()}))
    class Meta: #Meta is used to customize a models behavior
        model = Order
        fields = '__all__'
        exclude = ['customer', 'date_created',]
#used __all__ to get all the fields and exclude to not render certain fields


#This page is similar to forms.py