import unittest
from parameterized import parameterized

from main import min_of_three_vars


class MinOfThreeVarsTestCase(unittest.TestCase):

    @parameterized.expand([
        ("negative", (1, 2, 3), 1),
        ("integer", (2, 1, 3), 1),
        ("large fraction", (3, 2, 1), 1),
    ])
    def test_min_a(self, name, input, expected):
        self.assertEqual(min_of_three_vars(*input), expected)


        
