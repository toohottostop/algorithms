import unittest
from search_closest_number import search_closest


class TestClosestNumberInArray(unittest.TestCase):
    def test_find_closest(self):
        self.assertTrue(search_closest([], 50) == -1)
        self.assertTrue(search_closest([666], 555) == 666)
        self.assertTrue(search_closest([1, 2, 3, 4, 5, 6, 7], 6) == 6)
        self.assertTrue(search_closest([-150, -100, -50, 150, 200], -120) == -100)
        self.assertTrue(search_closest([100, 200, 300, 500], -50) == 100)
        self.assertTrue(search_closest([100, 200, 300, 500, 501], 50000) == 501)
        self.assertTrue(search_closest([x for x in range(0, 100000, 7)], 89000) == 88998)
        self.assertTrue(search_closest([1, 3, 5, 6, 50, 100], 51) == 50)
        self.assertTrue(search_closest([-1000, -500, -200, 0, 200, 500, 1000], -503) == -500)
