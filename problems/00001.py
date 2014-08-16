"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def main():
    sum_3 = sum_mult(3, 1000)
    sum_5 = sum_mult(5, 1000)
    sum_15 = sum_mult(15, 1000)

    print(sum_3 + sum_5 - sum_15)

def sum_mult(number, limit):
    """Sum of all multiples of number, upto limit"""

    count = 0
    sum_mult = 0
    mult = 0

    while mult < limit:
        sum_mult += mult
        count += 1
        mult = number*count
    print("count is: {}".format(count))
    print("sum is: {}".format(sum_mult))
    return sum_mult

if __name__ == '__main__':
    main()
