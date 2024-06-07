from .models import product
import django_filters


class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = product
        fields = '__all__'
        exclude = ["image","ava","descretion","name","discount","size","price"]


"""    
class orderFilter(django_filters.FilterSet):
    class Meta:
        model = order
        fields = '__all__'
        exclude = ["user","status","date","quantity"]
"""  