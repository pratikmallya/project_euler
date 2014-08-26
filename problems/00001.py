"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
import unittest

class Test(unittest.TestCase):

    def test_sample_cases(self):
        self.assertEqual(compute_ans(10), 23)
        self.assertEqual(compute_ans(100), 2318)


def compute_ans(limit):
    sum_3 = sum_mult(3, limit)
    sum_5 = sum_mult(5, limit)
    sum_15 = sum_mult(15, limit)
    return int(sum_3 + sum_5 - sum_15)


def sum_mult(number, limit):
    """Sum of all multiples of number, upto limit"""
    limit = limit - 1
    limit = (limit - (limit%number))/number
    return (number * limit * (limit+1))/2


if __name__ == '__main__':
    unittest.main()
