from rest_framework.viewsets import ModelViewSet
from .models import Mortgage
from .serializers import MortgageSerializer
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from .calculates import get_credit, get_validate_data

class MortgageFilter(filters.FilterSet):
    bank_name = filters.CharFilter(field_name="bank_name", lookup_expr='icontains', label='Название банка')

    rate_max = filters.NumberFilter(field_name="rate_max", lookup_expr='gt', label='Максимальная ставка меньше')
    rate_min = filters.NumberFilter(field_name="rate_min", lookup_expr='lt', label='Минимальная ставка больше')

    payment_max = filters.NumberFilter(field_name="payment_max", lookup_expr='gt', label='Максимальный платёж меньше')
    payment_min = filters.NumberFilter(field_name="payment_min", lookup_expr='lt', label='Минимальный платёж больше')

    class Meta:
        model = Mortgage
        fields = ['bank_name', 'rate_min', 'rate_max', 'payment_min', 'payment_max']

class MortgageViewSet(ModelViewSet):
    queryset = Mortgage.objects.all()
    serializer_class = MortgageSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = MortgageFilter

    def get_queryset(self):
        queryset = Mortgage.objects.all().order_by('rate_min')
        try:
            request = self.request.GET
            price, deposit, term = int(request.get('price')), int(request.get('deposit')), int(request.get('term'))
            if get_validate_data(price, term, deposit):
                credit = get_credit(price, deposit)
                queryset = Mortgage.objects.filter(payment_min__lte=credit, payment_max__gte=credit, term_min__lte=term, term_max__gte=term)
        except:
            pass
        finally:
            return queryset
    
