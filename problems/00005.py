"""
Project Euler, problem 5
https://www.hackerrank.com/contests/projecteuler/challenges/euler005
"""

from fractions import gcd
from sys import stdin
import unittest


class TestAlg(unittest.TestCase):

    def test_sample_case(self):
        input_nums = [3, 10]
        output_nums = [6, 2520]
        computed_nums = list(map(smallest_multiple, input_nums))
        self.assertEqual(output_nums, computed_nums)


def lcm(a, b):
    """Return the least common multiple of 2 integers

    lcm(a, b) * gcd(a, b) = a * b. Therefore, we can easily determine the lcm.

    Args:
        a, b: the integer whose lcm needs to be determined

    Returns:
        integer lcm of a and b
    """
    return (a * b) // gcd(a, b)


def smallest_multiple(N):
    """Compute the smallest multiple of range(N)

    An O(n) of doing this is as follows. Once you determine
    smallest_multiple(N), you can detemine smallest_multiple(N+1) as:

    smallest_multiple(N + 1) = lcm(smallest_multiple(N), N+1)

    Args:
        N: the limit of the natural number input sequence
    Returns:
        smallest multiple of range(N)
    """
    sm = 1
    for i in range(1, N+1):
        sm = lcm(i, sm)
    return sm


def main():
    T = int(stdin.readline())
    res = []
    for i in range(T):
        d = int(stdin.readline())
        res.append(smallest_multiple(d))

    for result in res:
        print(result)


if __name__ == '__main__':
    unittest.main()
