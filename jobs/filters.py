import django_filters
from django_filters import DateFilter, DateRangeFilter

from .models import *

class ProjectFilter(django_filters.FilterSet):
    #start_date = DateFilter(field_name="date_created", lookup_expr='gte)
    #end_date = DateFilter(field_name="date_created", lookup_expr='lte)
    
    class Meta:
        model = Project
        fields = '__all__'
        exclude = ['client','country','handled','type']

class TrackerFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="workedDate", lookup_expr='gte')
    end_date = DateFilter(field_name="workedDate", lookup_expr='lte')
    date_range = DateRangeFilter(field_name="workedDate")

    class Meta:
        model = Tracker
        fields = ['employee','client','job','status','activity','start_date','end_date','date_range','status']