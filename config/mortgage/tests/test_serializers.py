from unittest import TestCase
from mortgage.models import Mortgage
from mortgage.serializers import MortgageSerializer

class MortgageSerializerTest(TestCase):

    def test_serializer(self):
        mortgage = Mortgage.objects.create(
            bank_name = 'Test_bank_name1',
            term_min = 1,
            term_max = 2,
            rate_min = 1,
            rate_max = 2,
            payment_min = 1,
            payment_max = 2
        )

        data = MortgageSerializer(mortgage).data
        expected_data = {'id': mortgage.id,
                'payment': None,
                'bank_name': 'Test_bank_name1',
                'term_min': 1,
                'term_max': 2,
                'rate_min': 1.0,
                'rate_max': 2.0,
                'payment_min': 1,
                'payment_max': 2}

        self.assertDictEqual(expected_data, data)