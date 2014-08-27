from sys import stdin
from functools import reduce
from operator import mul
import unittest

class TestAlg(unittest.TestCase):
    def test_cc(self):
        max_range = 200000
        nums = [str(item) for item in range(1, max_range)]
        test_string = reduce(lambda x,y: x+y, nums)
        for i in range(1, max_range + 1):
            self.assertEqual(cc(i), int(test_string[i-1]))

    def test_compute_champerowne(self):
        d = list(range(1,8))
        cconst = compute_champernowne_const(d)
        self.assertEqual(cconst, 5040)

def main():
    T = int(stdin.readline())
    for i in range(T):
        d = map(int, stdin.readline().strip().split())
        print(compute_champernowne_const(d))

def compute_champernowne_const(d):
    return reduce(mul, map(cc, d))

def cc(num):
    ndigits = 1
    total_digits = 0

    while True:
        ndigit_numbers = 9 * 10**(ndigits-1)
        #total_digits = 10**(ndigits) - 1
        total_digits += ndigits*ndigit_numbers
        pos = total_digits - num
        if pos >= 0:
            break
        ndigits += 1

    #base_digits = 10**(ndigits-1) - 1
    base_digits = total_digits - ndigits*ndigit_numbers
    offset = num - base_digits - 1
    pos_number = str(int(offset/ndigits) + 10**(ndigits-1))
    pos_digit_pos = offset%ndigits
    return int(pos_number[pos_digit_pos])



if __name__ == "__main__":
    unittest.main()