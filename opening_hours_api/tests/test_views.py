import json

from django.test import TestCase, Client
from django.urls import reverse


class TestOpeningHours(TestCase):

    def setUp(self):
        self.client = Client()

    def test_opening_hours_api_for_full_week(self):
        with open('opening_hours_api/tests/full_week.json', 'r') as json_file:
            data_dict = json.load(json_file)
            data = data_dict.get('data')
            expected_result = data_dict.get('expected_result')

        response = self.client.post(reverse('opening_hours_api_view'), data=data, content_type='application/json')
        response_dict = response.data
        self.assertEqual(json.loads(response_dict), expected_result)

    def test_opening_hours_api_for_one_day(self):
        with open('opening_hours_api/tests/one_day.json', 'r') as json_file:
            data_dict = json.load(json_file)
            data = data_dict.get('data')
            expected_result = data_dict.get('expected_result')

        response = self.client.post(reverse('opening_hours_api_view'), data=data, content_type='application/json')
        response_dict = response.data
        self.assertEqual(json.loads(response_dict), expected_result)

    def test_opening_hours_api_for_partial_week(self):
        with open('opening_hours_api/tests/partial_week.json', 'r') as json_file:
            data_dict = json.load(json_file)
            data = data_dict.get('data')
            expected_result = data_dict.get('expected_result')

        response = self.client.post(reverse('opening_hours_api_view'), data=data, content_type='application/json')
        response_dict = response.data
        self.assertEqual(json.loads(response_dict), expected_result)
