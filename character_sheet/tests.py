from django.test import TestCase
from .calculations import calculate_ability_mod

# Create your tests here.
class CalculationTestCase(TestCase):
    def test_calculate_ability_mod(self):
        ability_score = 3
        self.assertEqual(calculate_ability_mod(ability_score), -3)
        ability_score = 11
        self.assertEqual(calculate_ability_mod(ability_score), 0)
        ability_score = 18
        self.assertEqual(calculate_ability_mod(ability_score), 4)
