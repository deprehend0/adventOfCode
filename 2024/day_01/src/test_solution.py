from unittest import TestCase
from solution import get_distance, calculate_total_distance


class Test(TestCase):

    def test_get_distance(self):
        assert get_distance(1, 2) == 1
        assert get_distance(2, 1) == 1


class Test(TestCase):
    def test_total_distance(self):

        left_list = [1, 2, 3, 3, 3, 4]
        right_list = [3, 3, 3, 4, 5, 9]
        assert calculate_total_distance(left_list, right_list).__eq__(11)
