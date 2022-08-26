from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
from mortgage.models import Mortgage

class MortgageListTest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        Mortgage.objects.create(
            id=1,
            bank_name = 'Test_bank_name1',
            term_min = 1,
            term_max = 2,
            rate_min = 1,
            rate_max = 2,
            payment_min = 1,
            payment_max = 2
        )
        Mortgage.objects.create(
            id=2,
            bank_name = 'Test_bank_name2',
            term_min = 1,
            term_max = 2,
            rate_min = 1,
            rate_max = 2,
            payment_min = 1,
            payment_max = 2
        )

    def test_list_mortgage(self):
        url = reverse('mortgage-list')
        response = self.client.get(url)
        data = response.data
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), Mortgage.objects.all().count())
    
    def test_retrieve_mortgage(self):
        payload={'id': 1,
                'payment': None,
                'bank_name': 'Test_bank_name1',
                'term_min': 1,
                'term_max': 2,
                'rate_min': 1.0,
                'rate_max': 2.0,
                'payment_min': 1,
                'payment_max': 2}
        url = reverse('mortgage-detail', kwargs={'pk': 1})
        response = self.client.get(url)
        data = response.data
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(data, payload)

    def test_create_mortgage(self):
        url = reverse('mortgage-list')
        payload={'bank_name': 'Test_bank_name',
                'term_min': '10',
                'term_max': '30',
                'rate_min': '1.8',
                'rate_max': '9.8',
                'payment_min': '1000000',
                'payment_max': '10000000'}
        start = Mortgage.objects.all().count()
        response = self.client.post(url, data=payload)
        data = response.data
        end = Mortgage.objects.all().count()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(end, start+1)
        self.assertEqual(data['bank_name'], 'Test_bank_name')
        self.assertIsNone(data['payment'])
        self.assertEqual(data['term_min'], 10)
        self.assertEqual(data['term_max'], 30)
        self.assertEqual(data['rate_min'], 1.8)
        self.assertEqual(data['rate_max'], 9.8)
        self.assertEqual(data['payment_min'], 1000000)
        self.assertEqual(data['payment_max'], 10000000)
    
    def test_delete_mortgage(self):
        url = reverse('mortgage-detail', kwargs={'pk': 1})
        start = Mortgage.objects.all().count()
        response = self.client.delete(url)
        end = Mortgage.objects.all().count()    
        self.assertEqual(end, start-1)    
        self.assertEqual(response.status_code, 204)
    
    def test_patch_mortgage(self):
        payload={'bank_name': 'Test_bank_name',
                'term_min': '10',
                'term_max': '30',
                'rate_min': '1.8',
                'rate_max': '9.8',
                'payment_min': '1000000',
                'payment_max': '10000000'}

        url = reverse('mortgage-detail', kwargs={'pk': 1})
        response = self.client.patch(url, data=payload)
        data = response.data
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['bank_name'], 'Test_bank_name')
        self.assertIsNone(data['payment'])
        self.assertEqual(data['term_min'], 10)
        self.assertEqual(data['term_max'], 30)
        self.assertEqual(data['rate_min'], 1.8)
        self.assertEqual(data['rate_max'], 9.8)
        self.assertEqual(data['payment_min'], 1000000)
        self.assertEqual(data['payment_max'], 10000000)
        