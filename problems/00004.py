import unittest
from sys import stdin


class Test(unittest.TestCase):

    def test_sample_cases(self):
        palindromes = compute_palindromes_fivesix()
        print("Total number of palindromes are {}".format(len(palindromes)))
        self.assertEqual(compute_three_digit_palindrome(palindromes,
                                                        101110), 101101)
        self.assertEqual(compute_three_digit_palindrome(palindromes,
                                                        800000), 793397)


def compute_palindromes_fivesix():
    """
    Compute all 5 and 6 digit palindromes
    """
    palindromes = []
    for i in range(1, 10):
        for j in range(10):
            for k in range(10):
                # 6 digit
                number_string = "{}{}{}{}{}{}".format(i, j, k, k, j, i)
                palindromes.append(int(number_string))
                # 5 digit
                number_string = "{}{}{}{}{}".format(i, j, k, j, i)
                palindromes.append(int(number_string))

    palindromes.sort(reverse=True)
    return palindromes


def compute_three_digit_palindrome(palindromes, maxnum):
    """
    Return the largest palindrome less than maxnum which can
    be split into 2 3 digit factors
    """
    tlist = list(map(lambda x: x < maxnum, palindromes))
    maxi = tlist.index(True)
    for palindrome in palindromes[maxi:]:
        if check_three_digit_palindrome(palindrome):
            return palindrome
    return None


def check_three_digit_palindrome(palindrome):
    """
    Check whether the palindrome can be factorized into 2 3 digit factors
    """
    for i in range(1, 10):
        for j in range(10):
            for k in range(10):
                number = int("{}{}{}".format(i, j, k))
                quotient = palindrome // number
                if len(str(quotient)) < 3:
                    return False
                if palindrome % number == 0:
                    if len(str(quotient)) == 3:
                            return True
    return False


def main():
    T = int(stdin.readline())
    palindromes = compute_palindromes_fivesix()
    for i in range(T):
        d = int(stdin.readline())
        print(compute_three_digit_palindrome(palindromes, d))

if __name__ == "__main__":
    unittest.main()
