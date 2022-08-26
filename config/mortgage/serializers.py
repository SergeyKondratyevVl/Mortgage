from rest_framework import serializers
from .models import Mortgage
from .calculates import get_credit, get_rate, calc_payment, get_validate_data

class MortgageSerializer(serializers.ModelSerializer):
    payment = serializers.SerializerMethodField(method_name='get_payment')
    class Meta:
        model = Mortgage
        fields = ('id',
        'payment',
        'bank_name',
        'term_min',
        'term_max',
        'rate_min',
        'rate_max',
        'payment_min',
        'payment_max')

    def get_payment(self, obj):
        try:
            request = self.context.get('request')
            price, deposit, term = int(request.GET.get('price')), int(request.GET.get('deposit')), int(request.GET.get('term'))
            if get_validate_data(price, term, deposit):
                credit = get_credit(price, deposit)
                rate = get_rate(obj.rate_min, obj.rate_max)
                payment = round(calc_payment(credit, term, rate))
            else:
                payment = 'Неверно введены данные'
        except:
            payment = None
        finally:
            return payment

