from unittest import TestCase
from mortgage.models import Mortgage

class MortgageModelTest(TestCase):

    def test_create_model(self):
        mortgage = Mortgage.objects.create(
            bank_name = 'Test_bank_name1',
            term_min = 1,
            term_max = 2,
            rate_min = 1,
            rate_max = 2,
            payment_min = 1,
            payment_max = 2
        )
        self.assertEqual(mortgage.bank_name, 'Test_bank_name1')
        self.assertEqual(mortgage.term_min, 1)
        self.assertEqual(mortgage.term_max, 2)
        self.assertEqual(mortgage.rate_min, 1.0)
        self.assertEqual(mortgage.rate_max, 2.0)
        self.assertEqual(mortgage.payment_min, 1)
        self.assertEqual(mortgage.payment_max, 2)
        