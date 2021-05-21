from unittest import TestCase
from search_pivot_point_in_shifted_array import app


class TestShiftedArray(TestCase):
    TEST_ARRAYS = ['[]',
                   '[1]',
                   '[1, -1]',
                   '[1, 2, 3, 5, -8, -6, -1, 0]',
                   '[2, 3, 4, 5, 0, 1]',
                   '[1, 2, 3, 4, -4, -3, -2, -1]',
                   '[1, 2, 3, 4, -1]',
                   '[3,99,-100,-1]']
    EXPECTED_PIVOT_POINTS = ['-1', '1', '1', '5', '5', '4', '4', '99']

    def setUp(self) -> None:
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/shifted_array/'

    def test_arrays(self):
        for array, expected_pivot in zip(self.TEST_ARRAYS, self.EXPECTED_PIVOT_POINTS):
            response = self.app.post(self.base_url, data=array)
            response_text = response.data.decode()

            self.assertEqual(response_text, expected_pivot)

    def test_big_data(self):
        big_numbers = f'{[it for it in range(10000001)] + [it for it in range(-4567890, 0, 1)]}'
        response = self.app.post(self.base_url, data=big_numbers)
        response_text = response.data.decode()

        self.assertEqual(response_text, '10000000')